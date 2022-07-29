
import React from "react";
import { Container, Row, Col } from 'react-bootstrap';
import './Footer.css';


class Footer extends React.Component {
    render() {
        return (
            <div className="footer bg-dark">
                <Container>
                    <Row>
                        <Col>
                            Ushi's Creations Brand Logo
                        </Col>
                        <Col>
                            Contact Links
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            © 2022 Copyright: Ushi's Creations.
                        </Col>
                    </Row>
                </Container>
            </div>
        );
    }
    
}

export default Footer;