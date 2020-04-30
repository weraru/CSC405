import React from 'react';
import { Modal, Button, Row, Col, Form } from 'react-bootstrap';


import EmployeePage from './EmployeePage';

export default function Indiv(props) {
    return (
      <Modal
        {  ...props} 
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header closeButton>
          <Modal.Title id="contained-modal-title-vcenter">
            Modal heading
          </Modal.Title>  
        </Modal.Header>
        <Modal.Body>
            <EmployeePage/>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="danger" onClick={props.onHide}>Close</Button>
        </Modal.Footer>
      </Modal>
    );
  }