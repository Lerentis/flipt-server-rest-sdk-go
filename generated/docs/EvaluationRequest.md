# EvaluationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RequestId** | Pointer to **string** |  | [optional] 
**NamespaceKey** | **string** |  | 
**FlagKey** | **string** |  | 
**EntityId** | **string** |  | 
**Context** | **map[string]string** |  | 
**Reference** | Pointer to **string** |  | [optional] 

## Methods

### NewEvaluationRequest

`func NewEvaluationRequest(namespaceKey string, flagKey string, entityId string, context map[string]string, ) *EvaluationRequest`

NewEvaluationRequest instantiates a new EvaluationRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEvaluationRequestWithDefaults

`func NewEvaluationRequestWithDefaults() *EvaluationRequest`

NewEvaluationRequestWithDefaults instantiates a new EvaluationRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRequestId

`func (o *EvaluationRequest) GetRequestId() string`

GetRequestId returns the RequestId field if non-nil, zero value otherwise.

### GetRequestIdOk

`func (o *EvaluationRequest) GetRequestIdOk() (*string, bool)`

GetRequestIdOk returns a tuple with the RequestId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestId

`func (o *EvaluationRequest) SetRequestId(v string)`

SetRequestId sets RequestId field to given value.

### HasRequestId

`func (o *EvaluationRequest) HasRequestId() bool`

HasRequestId returns a boolean if a field has been set.

### GetNamespaceKey

`func (o *EvaluationRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *EvaluationRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *EvaluationRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.


### GetFlagKey

`func (o *EvaluationRequest) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *EvaluationRequest) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *EvaluationRequest) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.


### GetEntityId

`func (o *EvaluationRequest) GetEntityId() string`

GetEntityId returns the EntityId field if non-nil, zero value otherwise.

### GetEntityIdOk

`func (o *EvaluationRequest) GetEntityIdOk() (*string, bool)`

GetEntityIdOk returns a tuple with the EntityId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntityId

`func (o *EvaluationRequest) SetEntityId(v string)`

SetEntityId sets EntityId field to given value.


### GetContext

`func (o *EvaluationRequest) GetContext() map[string]string`

GetContext returns the Context field if non-nil, zero value otherwise.

### GetContextOk

`func (o *EvaluationRequest) GetContextOk() (*map[string]string, bool)`

GetContextOk returns a tuple with the Context field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContext

`func (o *EvaluationRequest) SetContext(v map[string]string)`

SetContext sets Context field to given value.


### GetReference

`func (o *EvaluationRequest) GetReference() string`

GetReference returns the Reference field if non-nil, zero value otherwise.

### GetReferenceOk

`func (o *EvaluationRequest) GetReferenceOk() (*string, bool)`

GetReferenceOk returns a tuple with the Reference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReference

`func (o *EvaluationRequest) SetReference(v string)`

SetReference sets Reference field to given value.

### HasReference

`func (o *EvaluationRequest) HasReference() bool`

HasReference returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


