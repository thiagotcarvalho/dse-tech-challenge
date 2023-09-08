import React from 'react'
import {
  Alert,
  AlertIcon,
  AlertTitle,
  AlertDescription,
} from '@chakra-ui/react'

function AlertAction(props) {
  return (
    <>
      <Alert status='error'>
        <AlertIcon />
        <AlertTitle>{props.errorStatus}</AlertTitle>
        <AlertDescription>{props.errorStatusText}</AlertDescription>
      </Alert>
    </>
  )
}

export default AlertAction;