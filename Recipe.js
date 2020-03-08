import React from "react";   
import style from './recipe.module.css';

const Recipe = ({title, calories,image,ingredients})=>{
	return (
		<div className={style.recipe}>
			<h1>{title}</h1>
			<o1>
				{ingredients.map(ingredient => (
					<li>{ingredient.text}</li>
				))}
			</o1>
			<p>{calories}</p>
			<img className={style.image} src={image} alt="" />
		</div>
	);
};
export default Recipe;