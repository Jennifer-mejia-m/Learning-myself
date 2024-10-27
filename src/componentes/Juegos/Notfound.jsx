import { useRouteError } from "react-router-dom";

export default function notFound (){
    const error = useRouteError();
    console.error(error);

    return (
        <div id="error-page">
            <h2>Oops!</h2>
            <p>Lo siento, no podemos encontrar la página</p>
        </div>
    )
}