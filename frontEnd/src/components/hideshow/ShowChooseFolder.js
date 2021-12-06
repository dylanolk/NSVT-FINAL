// import React, { Component } from "react";

// export class ShowChooseFolder extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       open: false,
//     };
//     this.togglebutton = this.togglebutton.bind(this);
//   }
//   togglebutton() {
//     const { open } = this.state;
//     this.setState({
//       open: !open,
//     });
//   }
//   render() {
//     var { title, children } = this.props;
//     const { open } = this.state;
//     if (open) {
//       title = "Hide Folder Dialog";
//     } else {
//       title = "Show Folder Dialog";
//     }
//     return (
//       <div className="container">
//         <div style={{ marginTop: "10px" }}>
//           <div class="btn btn-secondary" onClick={this.togglebutton}>
//             {title}
//           </div>
//           {open && <div>{children}</div>}
//         </div>
//       </div>
//     );
//   }
// }
// export default ShowChooseFolder;
