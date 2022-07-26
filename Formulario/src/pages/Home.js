import { Link } from 'react-router-dom'

import banner from "../assets/banner.svg"
import features from "../assets/features.svg"

function Home(){
    return <div>
        <div className="section">
            <img src={banner} alt="banner" />
            <div className="content">
                <h1>Criar formularios  <span> Facil</span> </h1>
                <p>Monte campos, de  texto em area, nomes, emails   </p>
                <Link to="/create" className="btn">Começar</Link>
            </div>
        </div>
        <div className="section">
            <div className="content">
                <h1>UNIFEIFRC</h1>
            </div>
            <img src={features} alt="features" />
        </div>
    </div>
}

export default Home