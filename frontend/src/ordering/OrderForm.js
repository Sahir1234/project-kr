
import React from "react";
import { Container, Row, Col } from 'react-bootstrap';

class OrderForm extends React.Component {

  constructor(props) {
    super(props);
    this.state = {firstName: '', lastName: '', email: ''};

    this.handleFirstChange = this.handleFirstChange.bind(this);
    this.handleLastChange = this.handleLastChange.bind(this);
    this.handleEmailChange = this.handleEmailChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleFirstChange(event) {
    this.setState({firstName: event.target.value});
  }

  handleLastChange(event) {
    this.setState({lastName: event.target.value});
  }

  handleEmailChange(event) {
    this.setState({email: event.target.value});
  }

  handleSubmit(event) {
    alert('' + this.state.firstName + ' ' + this.state.lastName + ' ' + this.state.email + '');
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <br></br>
        <label>
          First Name:
          <input type="text" value={this.state.firstName} onChange={this.handleFirstChange} />
        </label>
        <br></br>
        <label>
          Last Name:
          <input type="text" value={this.state.lastName} onChange={this.handleLastChange} />
        </label>
        <br></br>
        <label>
          Email:
          <input type="text" value={this.state.email} onChange={this.handleEmailChange} />
        </label>
        <br></br>
        <input type="submit" value="Submit" />
      </form>
    );
  }

}
  
export default OrderForm;