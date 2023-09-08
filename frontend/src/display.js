import React from "react";
import {
    Box,
    Text,
} from '@chakra-ui/react'
import ExpandableProperty from "./expandable";

function DisplayData(props) {
    console.log('display', props.property);

    return (
        <Box
            color={'#666'}
            fontSize={'16px'}
            ml={'10px'}
            pt={'10px'}
            pl={'3px'}
        >
            {props.property ? (
                    typeof props.property === 'number' ||
                    typeof props.property === 'string' ||
                    typeof props.property === 'boolean' ? (
                        <React.Fragment>
                            <Text
                                color={'black'}
                                fontSize={'14px'}
                                fontWeight={'bold'}
                            >
                                {titleCase(props.propertyName)}: 
                            </Text>
                            {props.property.toString()}
                        </React.Fragment>
                    ) : (
                        <ExpandableProperty title={titleCase(props.propertyName)} expanded={!!props.rootProperty}>
                        {Object.values(props.property).map((property, index, { length }) => (
                            <DisplayData 
                                key={index}
                                property={property}
                                propertyName={Object.getOwnPropertyNames(props.property)[index]}
                            />
                        ))}
                        </ExpandableProperty>
                    )
            ) : (
                props.propertyName + ': property is empty'
            )}
        </Box>
    );    
};

const titleCase = (s) =>
  s.replace (/^[-_]*(.)/, (_, c) => c.toUpperCase())
   .replace (/[-_]+(.)/g, (_, c) => ' ' + c.toUpperCase())

export default DisplayData;