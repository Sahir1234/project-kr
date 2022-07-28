
import React from "react";
import { Container, Row, Col } from 'react-bootstrap';
import './Intro.css';

class Intro extends React.Component {
    render() {
        return (
            <Container>
                <Row id="introBox">
                    <Col>
                        <h2>
                            Welcome to Ushi's Creations!
                        </h2>
                        <br></br>
                        <p>
                            Description of the business
                        </p>
                    </Col>
                </Row>
            </Container>
        );
    }
}

export default Intro;