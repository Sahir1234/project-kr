
import React from 'react';
import Size from './Size.js';
import Color from './Color.js';
import Finish from './Finish.js';


class Catalog extends React.Component {
    render() {
        return (
            <div>
                <Size />
                <Color/>
                <Finish />
            </div>
        );
    }
    
  }
  
  export default Catalog;