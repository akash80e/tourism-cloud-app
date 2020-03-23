import React, {Component} from 'react'
import app from 'firebase/app';
import * as FirebaseUI from 'firebaseui';
import Firebase from '../Firebase';
import firebase from 'firebase'
import {Card, Container} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { withAuthorization} from '../Session';

const BookingPage = () => (
    <Container>
    <h1> Booking </h1>
    <Card as="button">
        <Card.Img  height="175"  variant="top" src="https://www.toronto.ca/wp-content/uploads/2020/03/94a1-emergency-home-page-skyline.jpg" />
        <Card.Body>
            <Card.Text>
            Toronto
            </Card.Text>
        </Card.Body>
    </Card>
    </Container>
)

const condition = authUser => !!authUser;

export default withAuthorization(condition)(BookingPage);
