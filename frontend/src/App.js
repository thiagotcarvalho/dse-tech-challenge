import React, { useState } from 'react';
import {
    Box,
    Button,
    Flex,
    Heading,
    Text,
    useDisclosure,
    VStack,
} from '@chakra-ui/react'
import CallAPIModal from './modal';

function App() {
    const { isOpen, onOpen, onClose } = useDisclosure();
    const [text, setText] = useState({
        title: '',
        body: '',
        url: '',
    });

    return (
        <Flex
            width={'100vw'}
            height={'100vh'}
            alignContent={'center'}
            justifyContent={'center'}
        >
            <Box 
                maxW={'2xl'}
                m={'0 auto'}
            >
                <Text
                    fontSize={'xl'}
                    fontFamily={'sans-serif'}
                    color={'#4F46E5'}
                    textAlign={'center'}
                    mt={'30px'}
                >
                    Finch
                </Text>
                <Heading
                    as={'h1'}
                    fontFamily={'sans-serif'}
                    textAlign={'center'}
                    fontSize={'4xl'}
                    mt={'10px'}
                >
                    Sandbox Lite
                </Heading>
                <VStack
                    spacing={5}
                    mt={'25px'}
                >
                    <Button
                        onClick={() => {
                                onOpen();
                                setText({
                                    title: 'Read Basic Company Data',
                                    body: 'Get basic company data from the selected provider.',
                                    url: 'http://localhost:8000/company/',
                                    label: 'Company',
                                    showInputField: false
                                });
                            }
                        }
                    >
                        Company
                    </Button>
                    <Button
                        onClick={() => {
                                onOpen();
                                setText({
                                    title: 'Read Company Directory and Organization Structure',
                                    body: 'Get company directory and organization structure for the selected provider.',
                                    url: 'http://localhost:8000/directory/',
                                    label: 'Directory',
                                    showInputField: false
                                });
                            }
                        }
                    >
                        Directory
                    </Button>
                    <Button
                        onClick={() => {
                                onOpen();
                                setText({
                                    title: 'Read Individual Data',
                                    body: 'Get individual data, excluding income and employment data for a specific employee from the selected provider.',
                                    url: 'http://localhost:8000/individual/',
                                    label: 'Individual',
                                    showInputField: true
                                });
                            }
                        }
                    >
                        Individual
                    </Button>
                    <Button
                        onClick={() => {
                                onOpen();
                                setText({
                                    title: 'Read Individual Employment and Income Data',
                                    body: 'Get individual employment and income data for a specific employee from the selected provider.',
                                    url: 'http://localhost:8000/employment/',
                                    label: 'Employment',
                                    showInputField: true
                                });
                            }
                        }
                    >
                        Employment
                    </Button>
                    <CallAPIModal
                        isOpen={isOpen}
                        onClose={onClose}
                        title={text.title}
                        body={text.body}
                        url={text.url}
                        label={text.label}
                        showInputField={text.showInputField}
                    />
                </VStack>
            </Box>
        </Flex>
    );
}

export default App;
