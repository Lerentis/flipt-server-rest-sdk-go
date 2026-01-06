# BatchEvaluationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RequestId** | Pointer to **string** |  | [optional] 
**Responses** | Pointer to [**[]EvaluationResponse**](EvaluationResponse.md) |  | [optional] 
**RequestDurationMillis** | Pointer to **float64** |  | [optional] 

## Methods

### NewBatchEvaluationResponse

`func NewBatchEvaluationResponse() *BatchEvaluationResponse`

NewBatchEvaluationResponse instantiates a new BatchEvaluationResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchEvaluationResponseWithDefaults

`func NewBatchEvaluationResponseWithDefaults() *BatchEvaluationResponse`

NewBatchEvaluationResponseWithDefaults instantiates a new BatchEvaluationResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRequestId

`func (o *BatchEvaluationResponse) GetRequestId() string`

GetRequestId returns the RequestId field if non-nil, zero value otherwise.

### GetRequestIdOk

`func (o *BatchEvaluationResponse) GetRequestIdOk() (*string, bool)`

GetRequestIdOk returns a tuple with the RequestId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestId

`func (o *BatchEvaluationResponse) SetRequestId(v string)`

SetRequestId sets RequestId field to given value.

### HasRequestId

`func (o *BatchEvaluationResponse) HasRequestId() bool`

HasRequestId returns a boolean if a field has been set.

### GetResponses

`func (o *BatchEvaluationResponse) GetResponses() []EvaluationResponse`

GetResponses returns the Responses field if non-nil, zero value otherwise.

### GetResponsesOk

`func (o *BatchEvaluationResponse) GetResponsesOk() (*[]EvaluationResponse, bool)`

GetResponsesOk returns a tuple with the Responses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponses

`func (o *BatchEvaluationResponse) SetResponses(v []EvaluationResponse)`

SetResponses sets Responses field to given value.

### HasResponses

`func (o *BatchEvaluationResponse) HasResponses() bool`

HasResponses returns a boolean if a field has been set.

### GetRequestDurationMillis

`func (o *BatchEvaluationResponse) GetRequestDurationMillis() float64`

GetRequestDurationMillis returns the RequestDurationMillis field if non-nil, zero value otherwise.

### GetRequestDurationMillisOk

`func (o *BatchEvaluationResponse) GetRequestDurationMillisOk() (*float64, bool)`

GetRequestDurationMillisOk returns a tuple with the RequestDurationMillis field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestDurationMillis

`func (o *BatchEvaluationResponse) SetRequestDurationMillis(v float64)`

SetRequestDurationMillis sets RequestDurationMillis field to given value.

### HasRequestDurationMillis

`func (o *BatchEvaluationResponse) HasRequestDurationMillis() bool`

HasRequestDurationMillis returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


