import React from "react";
import {
    Text,
} from '@chakra-ui/react'
import { 
    ChevronRightIcon,
    ChevronDownIcon,
} from '@chakra-ui/icons'


export default class ExpandableProperty extends React.Component {
    state = {
        isOpen: !!this.props.expanded
    };
  
    render() {
        return (
            <React.Fragment>
                <Text 
                    color={'#008080'}
                    cursor={'pointer'}
                    fontSize={'14px'}
                    fontWeight={'bold'}
                    onClick={() => this.setState({ isOpen: !this.state.isOpen })}
                >
                    {this.props.title}
                    {this.state.isOpen ? <ChevronRightIcon /> : <ChevronDownIcon />}
                </Text>
                {this.state.isOpen ? this.props.children : null}
                {React.Children.count(this.props.children) === 0 && this.state.isOpen ? 'Nothing here' : null}
            </React.Fragment>
        );
    }
}
  