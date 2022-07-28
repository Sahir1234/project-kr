import React from "react";
import { Container, Row, Col } from 'react-bootstrap';
import './Size.css';

class Size extends React.Component {
    render() {
        return (
            <Container>
                <Row id="sizeBox">
                    <Col>
                        We offer three sizes of coasters at this time: the small coaster, the 
                        medium coaster, and the large tray. To the right, you can see sample images of these
                        sizes as well as their dimensions.
                    </Col>
                    <Col>
                        image of small
                    </Col>
                    <Col>
                        image of large
                    </Col>
                    <Col>
                        image of tray
                    </Col>
                </Row>
            </Container>
        );
    }
}

export default Size;