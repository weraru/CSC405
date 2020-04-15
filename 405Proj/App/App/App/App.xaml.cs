using System;
using App.Pages;
using App.ViewModels;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace App
{
    public partial class App : Application
    {
        public  User User { get; internal set; }

        public App()
        {
            InitializeComponent();
            if(!Current.Properties.ContainsKey("LogoutTime"))
                MainPage = new NavigationPage(new LoginPage());
            else
            {
                if((TimeSpan)Current.Properties["LogoutTime"] < DateTime.Now.TimeOfDay)
                {
                    MainPage = new NavigationPage(new LoginPage());
                }
                else
                {
                    MainPage = new NavigationPage(new MainPage(User));
                }
            }
        }

        protected override void OnStart()
        {
        }

        protected override void OnSleep()
        {
        }

        protected override void OnResume()
        {
        }
    }
}
