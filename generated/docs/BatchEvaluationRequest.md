# BatchEvaluationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RequestId** | Pointer to **string** |  | [optional] 
**Requests** | [**[]EvaluationRequest**](EvaluationRequest.md) |  | 
**Reference** | Pointer to **string** |  | [optional] 

## Methods

### NewBatchEvaluationRequest

`func NewBatchEvaluationRequest(requests []EvaluationRequest, ) *BatchEvaluationRequest`

NewBatchEvaluationRequest instantiates a new BatchEvaluationRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchEvaluationRequestWithDefaults

`func NewBatchEvaluationRequestWithDefaults() *BatchEvaluationRequest`

NewBatchEvaluationRequestWithDefaults instantiates a new BatchEvaluationRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRequestId

`func (o *BatchEvaluationRequest) GetRequestId() string`

GetRequestId returns the RequestId field if non-nil, zero value otherwise.

### GetRequestIdOk

`func (o *BatchEvaluationRequest) GetRequestIdOk() (*string, bool)`

GetRequestIdOk returns a tuple with the RequestId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestId

`func (o *BatchEvaluationRequest) SetRequestId(v string)`

SetRequestId sets RequestId field to given value.

### HasRequestId

`func (o *BatchEvaluationRequest) HasRequestId() bool`

HasRequestId returns a boolean if a field has been set.

### GetRequests

`func (o *BatchEvaluationRequest) GetRequests() []EvaluationRequest`

GetRequests returns the Requests field if non-nil, zero value otherwise.

### GetRequestsOk

`func (o *BatchEvaluationRequest) GetRequestsOk() (*[]EvaluationRequest, bool)`

GetRequestsOk returns a tuple with the Requests field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequests

`func (o *BatchEvaluationRequest) SetRequests(v []EvaluationRequest)`

SetRequests sets Requests field to given value.


### GetReference

`func (o *BatchEvaluationRequest) GetReference() string`

GetReference returns the Reference field if non-nil, zero value otherwise.

### GetReferenceOk

`func (o *BatchEvaluationRequest) GetReferenceOk() (*string, bool)`

GetReferenceOk returns a tuple with the Reference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReference

`func (o *BatchEvaluationRequest) SetReference(v string)`

SetReference sets Reference field to given value.

### HasReference

`func (o *BatchEvaluationRequest) HasReference() bool`

HasReference returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


