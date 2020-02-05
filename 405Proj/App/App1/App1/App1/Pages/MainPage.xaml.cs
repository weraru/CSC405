using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;


namespace MainPage

{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            void OnButtonClicked(object sender, EventArgs e)
            {
                (sender as Button).Text = "On Break";
            }
        }
    }
}