import React, {Component} from 'react';
import {Link, withRouter} from 'react-router-dom';
import {Form, Button, Row, Col, Container, Image} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import {compose} from 'recompose'
import firebase from 'firebase'

import { withFirebase} from '../Firebase';
import * as ROUTES from '../../constants/routes';
import { SignUpLink} from '../SignUp'

const SignInPage = () => (
  <Container>
  <h1>SignIn</h1>
    <Row>
    <Col>
      <img src="https://www.kindpng.com/picc/m/19-190566_tourism-icon-tourism-hd-png-download.png" height='200' width='200' />
    </Col>
    <Col>
      <SignInForm />
      <SignUpLink />
    </Col>
    </Row>
  </Container>
);

const INITIAL_STATE = {
  email: '',
  password: '',
  error: null,
};


class SignInFormBase extends Component {
  constructor(props) {
    super(props);
    this.state = { ...INITIAL_STATE};
  }

  onSubmit = event => {
    const { email, password} = this.state;

    this.props.firebase
      .signIn(email, password)
      .then(authUser => {
        this.setState({...INITIAL_STATE});
        this.props.history.push(ROUTES.HOME);
      })
      .catch(error => {
        this.setState({error});
      });

      event.preventDefault();
  };

    googleSignIn = event => {
        var provider = new firebase.auth.GoogleAuthProvider();

        firebase.auth().signInWithPopup(provider)
        .then(function(result) {
          // This gives you a Google Access Token. You can use it to access the Google API.
          var token = result.credential.accessToken;
          // The signed-in user info.
          var user = result.user;
          // ...
        }).then(authUser => {
          this.setState({...INITIAL_STATE});
          this.props.history.push(ROUTES.HOME);
        })

        event.preventDefault();
    }


  onChange = event => {
    this.setState({ [event.target.name]: event.target.value});
  };

  render() {
    const {
      email,
      password,
      error
    } = this.state;

    const isInvalid =
         password === '' ||
         email === ''

    return (
        <Form onSubmit={this.onSubmit}>
        <Form.Label>Email</Form.Label>
        <Form.Control
          name="email"
          value={email}
          onChange={this.onChange}
          type="text"
          placeholder="Email Address"
        />
        <Form.Label className="mx-auto my-2">Password</Form.Label>
        <Form.Control
          name="password"
          value={password}
          onChange={this.onChange}
          type="password"
          placeholder="Password"
        />
        <Button className="mx-auto my-3" disabled={isInvalid} type="submit">Sign In</Button>
        
        {error && <p>{error.message}</p>}
        </Form>

    )
  }
}
const SignInForm = compose (
  withRouter,
  withFirebase,
)(SignInFormBase);


export default SignInPage;
export { SignInForm};
