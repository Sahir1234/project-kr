
import React from 'react';
import { Nav, Navbar, Container } from 'react-bootstrap';


class Header extends React.Component {
  render() {
    return (<Navbar bg="dark" expand="dark">
    <Container>
      <Navbar.Brand href="/">Site Name</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link href="/">Home</Nav.Link>
          <Nav.Link href="/order">Link</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Container>
  </Navbar>
    );
  }
}


export default Header;