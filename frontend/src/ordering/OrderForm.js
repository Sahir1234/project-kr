
import React from "react";
import { Container, Row, Col } from 'react-bootstrap';
import swal from 'sweetalert';
import CustomerInfo from './CustomerInfo.js';
import ProductOrder from './ProductOrder.js';
import './OrderForm.css';

class OrderForm extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      name: '', 
      email: '', 
      phone: '',
      order: {}
    };

    this.updateCustomerInfo= this.updateCustomerInfo.bind(this);
    this.validateEmail = this.validateEmail.bind(this);
    this.validatePhone = this.validatePhone.bind(this);
    this.validateState = this.validateState.bind(this);
    this.placeOrder = this.placeOrder.bind(this);
  }

  updateCustomerInfo(state) {
    this.setState( {name: state.name, email: state.email, phone: state.phone, order: this.state.order} );
  }

  validateEmail(email) {
    return /\S+@\S+\.\S+/.test(email);
  }

  validatePhone(phone) {
    return phone.match('[0-9]{10}');
  }

  validateState() {
    if (this.state.name === "") {
      swal("Oops!","Please enter a name for the order!", "error");
      return false;
    } else if (!this.validateEmail(this.state.email)) {
      swal("Oops!", "Please enter a valid email for the order!", "error");
      return false;
    } else if (!this.validatePhone(this.state.phone)) {
      swal("Oops!", "Please enter a valid phone number for the order!", "error");
      return false;
    }
    return true;
  }

  placeOrder() {
    if (this.validateState()) {

      // attempt to place order here 

      swal("Success!", "ORDER SUCCESSFULLY PLACED", "success");
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