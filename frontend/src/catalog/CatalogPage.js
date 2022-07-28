
import React from 'react';
import Intro from './Intro.js';
import Size from './Size.js';
import Color from './Color.js';
import Finish from './Finish.js';
import { Container, Row } from 'react-bootstrap';


class CatalogPage extends React.Component {
    render() {
        return (
            <Container>
                <br></br>
                <Row>
                    <Intro />
                </Row>
                <br></br>
                <Row>
                    <Size />
                </Row>
                <br></br>
                <Row>
                    <Color/>
                </Row>
                <br></br>
                <Row>
                    <Finish />
                </Row>
                <br></br>
            </Container>
        );
    }
    
  }
  
  export default CatalogPage;