using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Timers;
using App.Pages;
using App.ViewModels;
using Plugin.Permissions;
using Plugin.Permissions.Abstractions;
using Xamarin.Essentials;
using Xamarin.Forms;

namespace App
{
    [DesignTimeVisible(false)]
    public partial class MainPage : ContentPage
    {
        private Timer timer;

        public MainPage()
        {
            InitializeComponent();
            BindingContext = new MainViewModel();
            timer = new System.Timers.Timer();
            timer.Interval = 60000;

            timer.Elapsed += OnTimedEvent;
            timer.Enabled = true;

        }

        private void OnTimedEvent(object sender, ElapsedEventArgs e)
        {
            if (App.Current.Properties.ContainsKey("LogoutTime"))
            {
                if ((TimeSpan)App.Current.Properties["LogoutTime"] < DateTime.Now.TimeOfDay)
                {
                    App.Current.MainPage = new NavigationPage(new LoginPage());
                }
            }
        }
        
        
        protected override async void OnAppearing()
        {
            base.OnAppearing();
            //await RequestPermission();
        }
        private async Task RequestPermission()
        {
            try
            {
                var status = await CrossPermissions.Current.CheckPermissionStatusAsync(Permission.Location);
                if (status != PermissionStatus.Granted)
                {
                    Device.BeginInvokeOnMainThread(async () =>
                    {
                        if (await CrossPermissions.Current.ShouldShowRequestPermissionRationaleAsync(Permission.Location))
                        {
                            await DisplayAlert("Need location", "Need Location Permission", "OK");
                        }

                        var results = await CrossPermissions.Current.RequestPermissionsAsync(Permission.Location);
                        status = results[Permission.Location];
                    });
                }

                if (status == PermissionStatus.Granted)
                {

                }
                else if (status != PermissionStatus.Unknown)
                {

                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        void OnSaved_Clicked(System.Object sender, System.EventArgs e)
        {
            if(TP.Time != null)
            {
                App.Current.Properties["LogoutTime"] = TP.Time;
                App.Current.SavePropertiesAsync();
            }
        }
    }
}
