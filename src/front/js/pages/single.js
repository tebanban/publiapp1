import React, { useContext } from "react";
import PropTypes from "prop-types";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/SJ36-A_Garantias_Sociales.jpg";
import Card from "react-bootstrap/Card";

export const Single = props => {
	const { store, actions } = useContext(Context);
	const params = useParams();

	return (
		<Card>
			<Card.Header as="h5">{store.site[params.theid].title}</Card.Header>
			<Card.Body>
				<Card.Title>{store.site[params.theid].code}</Card.Title>

				<img src={rigoImageUrl} />

				<Link to="/app">
					<span className="btn btn-primary btn-lg" role="button">
						Back
					</span>
				</Link>
			</Card.Body>
		</Card>
	);
};

Single.propTypes = {
	match: PropTypes.object
};
