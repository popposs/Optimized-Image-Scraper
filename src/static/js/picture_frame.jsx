'use strict';

//Props: array of cat urls and index of currently displayed cat!
class Welcome extends React.Component {
    constructor(props) {
        super(props);
        this.state = { selected: 0 };
    }

    nextImage() {
        // console.log(this.state.selected);
        this.setState((prevState) => {
            return {'selected': prevState.selected + 1};
        });
    }

    prevImage() {
        // console.log(this.state.selected);
        this.setState((prevState) => {
            return {'selected': prevState.selected - 1};
        });
    }

    render() {
        return (
            <div>
                <button active={(this.state.selected >= 0).toString()} onClick={() => this.prevImage()}>Previous</button>
                <img src={this.props.urls[this.state.selected]} style={{width:"500px"}}/>
                <button active={(this.state.selected < this.props.urls.length).toString()} onClick={() => this.nextImage()}>Next</button>
            </div>
        );
    }
}

