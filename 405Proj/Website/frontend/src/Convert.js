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
      setAddress(responseJson.results[0].formatted_address)
      
})
  return(
    <TableCell align="left">{address}</TableCell>);
}