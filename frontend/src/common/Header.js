
import React from 'react';
import { Nav, Navbar, Container } from 'react-bootstrap';


class Header extends React.Component {

  render() {
    return (<Navbar collapseOnSelect expand="sm" variant="dark" bg="dark">
    <Container>
      <Navbar.Brand href="/">Ushi's Creations</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="ml-auto" activeKey={window.location.pathname}>
          <Nav.Link href="/">View Our Catalog</Nav.Link>
          <Nav.Link href="/order">Place An Order</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Container>
  </Navbar>
    );
  }
}


export default Header;