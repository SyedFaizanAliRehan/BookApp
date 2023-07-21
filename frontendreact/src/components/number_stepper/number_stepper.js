import './number_stepper.css'

function NumberStepper(props){
    return(
        <div className="numberStepper">
            <button>-</button>
            <input type="number"></input>
            <button>+</button>
        </div>
    )
}

export default NumberStepper;
