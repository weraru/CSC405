import React from 'react';
import {
    withGoogleMap,
    withScriptjs,
    GoogleMap,
    Marker,
    InfoWindow
  } from "react-google-maps"; 

function MapInit(props){
    const points = props.points;
    const defCenter = {lat: -92.610054, lng: 32.59556};

    return( 
        <GoogleMap 
            onLoad={map => {
                const bounds = new window.google.maps.LatLngBounds();
                map.fitBounds(bounds);
            }}
            defaultZoom = {14} 
            defaultCenter = {{lat:32.59556, lng:-92.610054}} 
        >
            {
                points.map(person => (
                    <Marker 
                        key= {person.name}
                        position={{
                            lat: parseInt(person.latitude),
                            lng: parseInt(person.longitude)
                        }}
                    />
                ))
            }
        </GoogleMap>

    )
}

const WrappedMap = withScriptjs(withGoogleMap(MapInit));
export default function Map(props){
    return (
    <div style={{width: "100vw", height: "50vh"}}>
        <WrappedMap 
            points={props.points}
            googleMapURL={`https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=${
                "AIzaSyDHskpHwGLtNYyH6tpbCbRYxFABpUDPTJo"
              }`}
            loadingElement ={<div style={{height: "100%"}}/>}
            containerElement={<div style={{ height: `100%` }} />}
            mapElement={<div style={{ height: `100%` }} />}
        />
    </div>
            )
}

