
import React from 'react';
import Size from './Size.js';
import Color from './Color.js';
import Finish from './Finish.js';
import { Container, Row } from 'react-bootstrap';


class CatalogPage extends React.Component {
    render() {
        return (
            <Container>
                <Row>
                    <Size />
                </Row>
                <Row>
                    <Color/>
                </Row>
                <Row>
                    <Finish />
                </Row>
            </Container>
        );
    }
    
  }
  
  export default CatalogPage;