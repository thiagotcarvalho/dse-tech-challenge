import React, { useState } from 'react';
import { Formik } from 'formik';
import {
    FormLabel,
    Input,
    FormControl,
    Button,
    Flex,
    Select,
    VStack,
} from '@chakra-ui/react';
import Axios from 'axios'
import DataDisplay from './display';
import AlertAction from './alert';

function CallAPIForm(props) {
    const [response, setResponse] = useState({});
    const [error, setError] = useState({})

    const fetchData = (formData, url) => {
        // clear error
        setError('');

        let payload = {
            provider_id: formData.provider_id,
            individual_id: formData.individual_id
        };
        console.log('DEBUG (payload): ', JSON.stringify(payload));

        Axios.post(url, payload).then((res) => {
            console.log('DEBUG (axios): ', res.data);
            setResponse(res.data);
        }).catch((error) => {
            console.log('DEBUG (error): ', error.response);
            setError(error.response);
        });
    }

    const showInputField = props.showInputField;

    return (
        <Flex
            width={'100vw'}
            alignContent={'center'}
            justifyContent={'center'}
        >
            <VStack>
                <Formik
                    initialValues={{ individual_id: '', provider_id: ''}}
                    onSubmit={(values, { setSubmitting }) => {
                        fetchData(values, props.url);
                        setSubmitting(false);
                    }}
                >
                    {({ values, handleChange, handleBlur, handleSubmit, isSubmitting }) => (
                        <form onSubmit={handleSubmit}>
                            <FormControl as='fieldset'>
                                <Select placeholder='Select a provider' name='provider_id' onChange={handleChange} value={values.provider_id}>
                                    <option value='adp_run'>ADP Run</option>
                                    <option value='bamboo_hr'>Bamboo HR</option>
                                    <option value='bamboo_hr_api'>Bamboo HR (API)</option>
                                    <option value='bob'>HiBob</option>
                                    <option value='gusto'>Gusto</option>
                                    <option value='humaans'>Humaans</option>
                                    <option value='insperity'>Insperity</option>
                                    <option value='justworks'>Justworks</option>
                                    <option value='namely'>Namely</option>
                                    <option value='paychex_flex'>Paychex Flex</option>
                                    <option value='paychex_flex_api'>Paychex Flex (API)</option>
                                    <option value='paycom'>Paycom</option>
                                    <option value='paycom_api'>Paycom (API)</option>
                                    <option value='paylocity'>Paylocity</option>
                                    <option value='paylocity_api'>Paylocity (API)</option>
                                    <option value='personio'>Personio</option>
                                    <option value='quickbooks'>Quickbooks</option>
                                    <option value='rippling'>Rippling</option>
                                    <option value='sage_hr'>Sage HR</option>
                                    <option value='sapling'>Sapling</option>
                                    <option value='sequoia_one'>Squoia One</option>
                                    <option value='square_payroll'>Square Payroll</option>
                                    <option value='trinet'>Trinet</option>
                                    <option value='trinet_api'>Trinet (API)</option>
                                    <option value='ulti_pro'>Ulti Pro</option>
                                    <option value='wave'>Wave</option>
                                    <option value='workday'>Workday</option>
                                    <option value='zenefits'>Zenefits</option>
                                    <option value='zenefits_api'>Zenefits (API)</option>
                                </Select>
                                {showInputField && <FormLabel mt={5}>Individual Id:</FormLabel>}
                                {showInputField && <Input name='individual_id' onChange={handleChange} onBlur={handleBlur} value={values.individual_id}></Input>}
                            </FormControl>
                            <Button
                                mt={4}
                                disabled={isSubmitting}
                                type='submit'
                            >
                                Submit
                            </Button>
                        </form>
                    )}
                </Formik>
                <DataDisplay 
                    property={response}
                    propertyName={props.label + '_data'}
                    rootProperty={true}
                />
                {error.status && <AlertAction mt={'30px'} errorStatus={error.status} errorStatusText={error.statusText}/>}
            </VStack>
        </Flex>
    )
}

export default CallAPIForm;