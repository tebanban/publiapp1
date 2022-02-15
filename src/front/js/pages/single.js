import React, { useContext } from "react";
import PropTypes from "prop-types";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/SJ36-A_Garantias_Sociales.jpg";
import { Card, Image, Col, Row, Form } from "react-bootstrap";

export const Single = props => {
	const { store, actions } = useContext(Context);
	const params = useParams();

	return (
		<div>
			<Card.Header as="h5">{store.site[params.theid].title}</Card.Header>
			<Card.Body>
				<Card.Title>{store.site[params.theid].code}</Card.Title>
				<Form>
					<Row>
						<Col md={3}>
							<Image src={rigoImageUrl} fluid="true" />
						</Col>
						<Col md={9}>
							<Form.Group>
								<label htmlFor="inputAddress">Propietario</label>
								<input type="text" className="form-control" id="inputAddress" placeholder=""></input>
							</Form.Group>
							<Form.Group>
								<label htmlFor="inputAddress">Dirección</label>
								<input type="text" className="form-control" id="inputAddress" placeholder=""></input>
							</Form.Group>
							<Form.Group>
								<label htmlFor="inputAddress">Teléfono</label>
								<input type="text" className="form-control" id="inputAddress" placeholder=""></input>
							</Form.Group>
							<Form.Group>
								<label htmlFor="inputAddress">Email</label>
								<input type="text" className="form-control" id="inputAddress" placeholder=""></input>
							</Form.Group>
						</Col>
					</Row>
				</Form>
			</Card.Body>
			<Link to="/app">
				<span className="btn btn-primary btn-lg" role="button">
					Back
				</span>
			</Link>
		</div>
	);
};

Single.propTypes = {
	match: PropTypes.object
};
