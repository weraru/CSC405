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

        public ICommand EmergencyCommand { protected set; get; }


        ObservableCollection<LatLon> _LatLonCollection;
        private Timer aTimer;
        private Timer bTimer;
        private string _BreakText = "Break";
        private string _EmergencyText = "Emergency";


        public MainViewModel()
        {
            ProfileCommand = new Command(OnProfileClicked);
            BreakCommand = new Command(OnBreakClicked);
            EmergencyCommand = new Command(OnEmergencyClicked);
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
            if (BreakText != "On Break")
            {
                BreakText = "On Break";
                EnableTimers(false);
            }
            else
            {
                BreakText = "Break";
                EnableTimers(true);
            }
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

        private void OnEmergencyClicked(object obj)
        {
            if (BreakText != "In Emergency")
            {
                BreakText = "In Emergency";
                EnableTimers(true);
            }
            else
            {
                BreakText = "Emergency";
                EnableTimers(true);
            }
        }

        private void OnTimedGetLocationEvent(object sender, ElapsedEventArgs e)
        {

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
        public string BreakText
        {
            get { return _BreakText; }
            set
            {
                _BreakText = value;
                PropertyChanged(this, new PropertyChangedEventArgs("BreakText"));
            }
        }
        public string EmergencyText
        {
            get { return _EmergencyText; }
            set
            {
                _EmergencyText = value;
                PropertyChanged(this, new PropertyChangedEventArgs("EmergencyText"));
            }
        }
    }
}
