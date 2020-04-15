using System;
using System.ComponentModel;
using System.Windows.Input;
using Xamarin.Forms;
using System.Net.Http;
using System.Collections.Generic;
using Newtonsoft.Json;
using System.Diagnostics;
using System.Text;
using GalaSoft.MvvmLight.Views;


namespace App.ViewModels
{
    public class LoginViewModel : INotifyPropertyChanged
    {
        HttpClientHandler clientHandler = new HttpClientHandler();
       
        private HttpClient client = new HttpClient(new System.Net.Http.HttpClientHandler());
        public Action DisplayInvalidLoginPrompt;
        public event PropertyChangedEventHandler PropertyChanged = delegate { };
        private string email = "run";
        public string id = "hi";
        public string Email
        {
            get { return email; }
            set
            {
                email = value;
                PropertyChanged(this, new PropertyChangedEventArgs("Email"));
            }
        }
        
private string password = "free";
        public string Password
        {
            get => password;
            set
            {
                password = value;
                PropertyChanged(this, new PropertyChangedEventArgs("Password"));
            }
        }
        public ICommand SubmitCommand { protected set; get; }
        public LoginViewModel()
        {
            SubmitCommand = new Command(OnSubmit);
        }
        public async void OnSubmit()
        {
           
            string user = Newtonsoft.Json.JsonConvert.SerializeObject(new
            {

                username = email,
                password = password,
            });
            var content = new StringContent(user, Encoding.UTF8, "application/json");


            //string jsonString = Newtonsoft.Json.JsonConvert.SerializeObject(user);
            //var content = new FormUrlEncodedContent(jsonString);
            clientHandler.ServerCertificateCustomValidationCallback += (sender, cert, chain, sslPolicyErrors) => { return true; };
            client = new HttpClient(clientHandler);
            var response = await client.PostAsync("https://162.236.218.100:5005/login", content);
            var result = response.Content.ReadAsStringAsync().Result;
            Debug.WriteLine("hero main" + result);
            if (email=="0")
            {
                DisplayInvalidLoginPrompt();
            }
            else
            {
                 User U = new User
                {
                    username = email,
                    password = password,
                    id = result
                };
               

               App.Current.MainPage = new NavigationPage(new MainPage(U));
            }
        }
        
    }
    public  partial class User 
        {
        public string username { get; set; }
        public string password { get; set; }
        
        public string id { get; set; }


       }
        
}
