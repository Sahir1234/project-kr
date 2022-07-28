
import React from "react";
import { Container, Row, Col } from 'react-bootstrap';
import './Finish.css';

class Finish extends React.Component {
    render() {
        return (
            <Container>
                <Row id="finishBox">
                    <Col>
                        For all of our coasters, we apply a finish on the edges to give it
                        a clean, polished look. There are two options for the finish: gold and
                        silver. We have some examples here to compare the two finish colors.
                    </Col>
                    <Col>
                        gold picture
                    </Col>
                    <Col>
                        silver pic
                    </Col>
                </Row>
            </Container>
        );
    }
}

export default Finish;