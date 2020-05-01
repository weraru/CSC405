import React from 'react';
import { Modal, Button, Row, Col, Form } from 'react-bootstrap';



export default function FailLogin(props) {
    return (
      <Modal
        {  ...props} 
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header closeButton>
          <Modal.Title id="contained-modal-title-vcenter">
            Login Failed
          </Modal.Title>  
        </Modal.Header>
        <Modal.Body>
            Invalid login data
        </Modal.Body>
        <Modal.Footer>
          <Button variant="danger" onClick={props.onHide}>Close</Button>
        </Modal.Footer>
      </Modal>
    );
  }