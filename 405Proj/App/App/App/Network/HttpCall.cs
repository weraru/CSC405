using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

namespace App.Network
{
    public class HttpCall
    {
        private static readonly HttpClient client = new HttpClient();
        public static async Task<string> CallNetwork(LatLon latLon)
        {
            var values = new Dictionary<string, string>
            {
                { "Latitude", latLon.Latitude },
                { "Longitude", latLon.Longitude }
            };

            var content = new FormUrlEncodedContent(values);
            var url = "http://www.example.com/endpoint";
            var response = await client.PostAsync(url, content);

            return await response.Content.ReadAsStringAsync();
        }
    }
}
