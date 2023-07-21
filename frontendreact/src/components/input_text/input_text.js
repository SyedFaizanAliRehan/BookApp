import './input_text.css'

function InputText(props){
    return(
        <div className="input_field">
            <input type={props.type} id={props.id} name={props.name} placeholder={props.label}></input>
            <label for={props.id}>{props.label}</label>
        </div>
    )
}
export default InputText;
