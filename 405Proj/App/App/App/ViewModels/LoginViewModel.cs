using System;
using System.ComponentModel;
using System.Windows.Input;
using Xamarin.Forms;
using System.Net.Http;
using System.Collections.Generic;


namespace App.ViewModels
{
    public class LoginViewModel : INotifyPropertyChanged
    {
        private static readonly HttpClient client = new HttpClient();
        public Action DisplayInvalidLoginPrompt;
        public event PropertyChangedEventHandler PropertyChanged = delegate { };
        private string email = "watchmen@gmail.com";
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
        private string password = "secret";
        public string Password
        {
            get { return password; }
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
           // var values=new JavaScriptSerializer().Serialize({username, password});
           // var content = new FormUrlEncodedContent(values);
           // var response = await client.PostAsync("162.236.218.100:500/login", content);
            if (email != "watchmen@gmail.com" || password != "secret")
            {
                DisplayInvalidLoginPrompt();
            }
            else
            {
                App.Current.MainPage = new NavigationPage(new MainPage());
            }
        }
    }
}
