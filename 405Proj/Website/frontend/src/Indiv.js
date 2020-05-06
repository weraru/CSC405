import React from 'react';
import { Modal, Button, Row, Col, Form } from 'react-bootstrap';



import Map from './Map';

export default function Indiv(props) {
    const heading = props.heading;
    return (
      <Modal
        {  ...props} 
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header closeButton>
          <Modal.Title id="contained-modal-title-vcenter">
            {heading}
          </Modal.Title>  
        </Modal.Header>
        <Modal.Body>
            <Map
            
            />
        </Modal.Body>
        <Modal.Footer>
          <Button variant="danger" onClick={props.onHide}>Close</Button>
        </Modal.Footer>
      </Modal>
    );
  }