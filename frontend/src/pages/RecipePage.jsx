import { Link } from 'react-router-dom';
import './RecipePage.css';
import Recipes from '../components/Recipes';
import { Row, Col } from 'react-bootstrap';

function RecipePage() {
	return (
		<div className="Recipe">
			<Row>
				<Col md="10">
					<Recipes />
				</Col>
				<Col md="2">
					<div>
						<Link to="/ingredients">Ingredients</Link>
					</div>

					<div>
						<Link to="/recipes/create">Create Recipe</Link>
					</div>
				</Col>
			</Row>

			{/* <Link to="/ingredients">All Ingredients</Link>
			<Link to="/ingredients/create">Add Ingredient</Link>
			<Link to="/recipes">All Recipes</Link>
			<Link to="/recipes/create">Create Recipe</Link> */}
		</div>
	);
}

export default RecipePage;