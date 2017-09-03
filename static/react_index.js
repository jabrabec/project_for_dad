class Reading extends React.Component {
  constructor(props) {
    super(props);
    this.state = {data: ""};
  }

  componentDidMount() {
    setInterval(() => this.getCurrentData(), 250);
  }

  getCurrentData () {
    const react = this;
    axios.get("http://localhost:5000/read-file.json"
      ).then(function (response) 
        {if (response.status === 200)
          {react.setState({data: response.data})};
        }
      ).catch(function (error) {console.log(error);
      })
  }

  render() {
    return (
        <div>
          <p>{this.state.data}</p>
        </div>
    );
  }

}

ReactDOM.render(<Reading/>,document.getElementById('main-div'))
