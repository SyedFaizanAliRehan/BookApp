import './App.css';
import 'react-bootstrap';
import InputText from './components/input_text/input_text';
import NumberStepper from './components/number_stepper/number_stepper';


function App() {
  return (
    <div className="App">
      <body>
        <InputText id="username" label="Username" type="text"></InputText>
        <NumberStepper></NumberStepper>
      </body>
    </div>
  );
}

export default App;
