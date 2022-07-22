
import React from 'react';
import OrderForm from './OrderForm.js'
import { Container } from 'react-bootstrap';

class OrderPage extends React.Component {
    
    render() {
        return (
            <Container>
                <OrderForm />
            </Container>
        );
    }
}

export default OrderPage;