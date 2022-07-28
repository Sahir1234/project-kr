
import React from "react";
import { Container, Row, Col, Alert } from 'react-bootstrap';
import CustomerInfo from './CustomerInfo.js';
import ProductOrder from './ProductOrder.js';
import './OrderForm.css';

class OrderForm extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      alertShow: true,
      alertMessage: 'asffdsas',
      name: '', 
      email: '', 
      phone: ''
    };

    this.updateCustomerInfo= this.updateCustomerInfo.bind(this);
    this.validateEmail = this.validateEmail.bind(this);
    this.validatePhone = this.validatePhone.bind(this);
    this.validateState = this.validateState.bind(this);
    this.placeOrder = this.placeOrder.bind(this);
  }

  updateCustomerInfo(state) {
    this.setState( {name: state.name, email: state.email, phone: state.phone} );
  }

  validateEmail(email) {
    return /\S+@\S+\.\S+/.test(email);
  }

  validatePhone(phone) {
    return true;
  }

  validateState() {
    if (this.state.name === "") {
      alert("Please enter a name for the order!");
      return false;
    } else if (this.state.email === "" || !this.validateEmail(this.state.email)) {
      alert("Plase enter a valid email for the order!");
      return false;
    } else if (this.state.phone === "" || !this.validatePhone(this.state.phone)) {
      alert("Pleae enter a valid phone number for the order!");
      return false;
    }
    return true;
  }

  placeOrder() {
    if (this.validateState()) {
      alert ("ORDER SUCCESSFULLY PLACED");
    }
  }

  render() {
    return (
      <Container>
        <Row>
          <CustomerInfo updateInfo={this.updateCustomerInfo} />
        </Row>
        <br></br>
        <Row>
          <ProductOrder />
        </Row>
        <br></br>
        <Row id="submissionBox">
          <Col>
            Please double check all of your order information before submitting.
            We will email you an order confirmation shortly after you place your order
            with instructions for payment and delivery. Thank you!
          </Col>
          <Col>
            <button id="submitButton" onClick={this.placeOrder}>Place Order</button>
          </Col>
        </Row>
      </Container>
    );
  }

}
  
export default OrderForm;