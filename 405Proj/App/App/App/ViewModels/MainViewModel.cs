using System;
using System.Linq;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Timers;
using System.Windows.Input;
using App.Network;
using App.Pages;
using Xamarin.Essentials;
using Xamarin.Forms;

namespace App.ViewModels
{
    public class MainViewModel : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler PropertyChanged = delegate { };
        public ICommand ProfileCommand { protected set; get; }
        public ICommand BreakCommand { protected set; get; }

        public string Onbreak = "No";

        ObservableCollection<LatLon> _LatLonCollection;
        private Timer aTimer;
        private Timer bTimer;

        public MainViewModel()
        {
            ProfileCommand = new Command(OnProfileClicked);
            BreakCommand = new Command(OnBreakClicked);
            LatLonCollection = new ObservableCollection<LatLon>();
            aTimer = new Timer();
            aTimer.Elapsed += new ElapsedEventHandler(OnTimedGetLocationEvent);
            aTimer.Interval = 3000;
            bTimer = new Timer();
            bTimer.Elapsed += new ElapsedEventHandler(OnTimedHttpCallEvent);
            bTimer.Interval = 4000;
            EnableTimers(true);
        }

        private void OnBreakClicked(object obj)
        { 
            Obreak();
        }

        private async void OnProfileClicked(object obj)
        {
            await App.Current.MainPage.Navigation.PushModalAsync(new ProfilePage());
        }
 
        

        internal void EnableTimers(bool b)
        {
            aTimer.Enabled = b;
            bTimer.Enabled = b;
        }
        private void OnTimedGetLocationEvent(object sender, ElapsedEventArgs e)
        {
            if (Onbreak == "No")
                try
                {
                    Device.BeginInvokeOnMainThread(async () =>
                    {
                        var request = new GeolocationRequest(GeolocationAccuracy.Medium);
                        var location = await Geolocation.GetLocationAsync(request);

                        if (location != null)
                        {
                            LatLonCollection.Insert(0, new LatLon { Latitude = location.Latitude.ToString(), Longitude = location.Longitude.ToString() });
                            Console.WriteLine($"Latitude: {location.Latitude}, Longitude: {location.Longitude}, Altitude: {location.Altitude}");
                        }
                    });
                }
                catch (FeatureNotSupportedException fnsEx)
                {
                    // Handle not supported on device exception
                    Console.WriteLine(fnsEx.Message);
                }
                catch (FeatureNotEnabledException fneEx)
                {
                    // Handle not enabled on device exception
                    Console.WriteLine(fneEx.Message);
                }
                catch (PermissionException pEx)
                {
                    // Handle permission exception
                    Console.WriteLine(pEx.Message);
                }
                catch (Exception ex)
                {
                    // Unable to get location
                    Console.WriteLine(ex.Message);
                }

        }
        private async void OnTimedHttpCallEvent(object sender, ElapsedEventArgs e)
        {
            //Remove RETURN statement when API endpoint is ready
            return;

            if (LatLonCollection.Any())
                await HttpCall.CallNetwork(LatLonCollection[0]);
        }
        public ObservableCollection<LatLon> LatLonCollection
        {
            get { return _LatLonCollection; }
            set
            {
                _LatLonCollection = value;
                PropertyChanged(this, new PropertyChangedEventArgs("LatLonCollection"));
            }
        }
        public void Obreak()
        {
            if (Onbreak == "No")
            {
                Onbreak = "Yes";
            }
            else
            {
                Onbreak = "No";
            }
        }
    }
}
  

