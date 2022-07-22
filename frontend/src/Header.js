
import './Header.css';
import { Link, useMatch, useResolvedPath } from "react-router-dom";

function Header() {
    return (<nav className="nav">
      <div className="site-title">
        Site Name
      </div>
      <ul>
        <CustomLink to="/">View Products</CustomLink>
        <CustomLink to="/order">Place an Order</CustomLink>
      </ul>
    </nav>
    )
}

function CustomLink({ to, children, ...props }) {
    const resolvedPath = useResolvedPath(to)
    const isActive = useMatch({ path: resolvedPath.pathname, end: true })
  
    return (
      <li className={isActive ? "active" : ""}>
        <Link to={to} {...props}>
          {children}
        </Link>
      </li>
    )
}

export default Header;