import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
} from '@chakra-ui/react'
import CallAPIForm from './form';

function CallAPIModal(props) {
    return (
        <>  
            <Modal isOpen={props.isOpen} onClose={props.onClose} size={'lg'}>
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader>{props.title}</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>{props.body}</ModalBody>
                    
                    <ModalFooter>
                        <CallAPIForm
                            url={props.url}
                            label={props.label}
                            showInputField={props.showInputField}
                        />
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </>
    )
}

export default CallAPIModal;