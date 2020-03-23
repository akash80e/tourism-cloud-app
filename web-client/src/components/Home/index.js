import React from 'react';
import { withAuthorization} from '../Session';
import {Form, Button, Container} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const HomePage = () => (
    <Container>
        <h1>Home Page</h1>
            <Form >
                <Form.Group controlId="exampleForm.ControlInput1">
                    <Form.Label>Enter a tourist spot</Form.Label>
                    <Form.Control name="keyword_book" placeholder="e.g. Toronto" />
                </Form.Group>
                <Button variant="primary" >Search</Button>
            </Form>
        <hr/>
    </Container>
);

const condition = authUser => !!authUser;

export default withAuthorization(condition)(HomePage);
