
import React from "react";
import { Container, Row, Col } from 'react-bootstrap';
import './CustomerInfo.css';

class CustomerInfo extends React.Component {

    constructor(props) {
        super(props);
        this.state = {name: '', email: '', phone: ''}
    
        this.handleNameChange = this.handleNameChange.bind(this);
        this.handleEmailChange = this.handleEmailChange.bind(this);
        this.handlePhoneChange = this.handlePhoneChange.bind(this);
      }
    
      handleNameChange(event) {
        this.setState( {name: event.target.value, email: this.state.email, phone: this.state.phone} );
        this.props.updateInfo(this.state);
      }
    
      handleEmailChange(event) {
        this.setState( {name: this.state.name, email: event.target.value, phone: this.state.phone} );
        this.props.updateInfo(this.state);
      }

      handlePhoneChange(event) {
        this.setState( {name: this.state.name, email: this.state.email, phone: event.target.value} );
        this.props.updateInfo(this.state);
      }


    render() {
        return (
            <Container>
            <Row id="customerInfoBox">
                <Col>
                    <label>
                    <div>Name: </div>
                    <input type="text" value={this.state.name} onChange={this.handleNameChange} />
                    </label>
                  </Col>
                  <Col>
                    <label>
                    <div>Email: </div>
                    <input type="text" value={this.state.email} onChange={this.handleEmailChange} />
                    </label>
                  </Col>
                  <Col>
                    <label>
                    <div>Phone Number: </div>
                    <input type="text" value={this.state.phone} onChange={this.handlePhoneChange} />
                    </label>
                </Col>
            </Row>
            </Container>
        );
    }
    
}

export default CustomerInfo;