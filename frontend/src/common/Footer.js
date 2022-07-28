
import React from "react";
import { Container, Row, Col } from 'react-bootstrap';


class Footer extends React.Component {
    render() {
        return (
            <Container>
                <Row>
                    <Col></Col>
                    <Col>
                        Brand logo
                    </Col>
                    <Col>
                        contact us
                    </Col>
                    <Col></Col>
                </Row>
                <div className="footer-bottom">
                    <p className="text-xs-center">
                        Put Copyright and trademark stuff here
                    </p>
                </div>
                
            </Container>
            
        );
    }
    
}

export default Footer;