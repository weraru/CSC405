import React from 'react';
import ReactDOM from 'react-dom';
import TableCell from '@material-ui/core/TableCell';

export default function Convert(props){
    const {latitude, longitude} = props;
    const [address, setAddress] = React.useState();


  const KEY = "AIzaSyDHskpHwGLtNYyH6tpbCbRYxFABpUDPTJo";
  fetch('https://maps.googleapis.com/maps/api/geocode/json?address=' + latitude + ',' + longitude + '&key=' + KEY)
  .then((response) => response.json())
  .then((responseJson) => {
      console.log(JSON.stringify(responseJson.results[0].formatted_address))
      setAddress(responseJson.results[0].formatted_address)
      
})
  console.log(address);
  return(
    <TableCell align="left">{address}</TableCell>);
}