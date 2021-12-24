import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

import "../../styles/app.scss";
import { Col, Container, Row } from "react-bootstrap";

export const App = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container">
			<div className="container">
				<div className="listheader list-group-item d-flex justify-content-between">
					<div className="col-1 ">img</div>
					<div className="col-1"> Código </div>
					<div className="col-3"> Nombre</div>
					<div className="col-3"> Ubicación</div>
					<div className="col-3"> Contacto</div>
					<div className="col-1"> Accion</div>
				</div>
				{store.site.map((item, index) => {
					return (
						<div
							key={index}
							className="list-group-item d-flex justify-content-between"
							style={{ background: item.background }}>
							<div className="col-1"> img </div>
							<div className="col-1">
								<Link to={"/single/" + index}>
									<span>{item.code}</span>
								</Link>
							</div>

							<div className="col-3">{item.title}</div>
							<div className="col-3">{item.address}</div>
							<div className="col-3">{item.contact}</div>

							<div className="col-1 btn btn-success" type="button">
								<Link to={"/single/" + index} className="link">
									<span>VER</span>
								</Link>
							</div>
						</div>
					);
				})}
			</div>
			<br />
			<Link to="/">
				<button className="btn btn-primary">Back home</button>
			</Link>
		</div>
	);
};
