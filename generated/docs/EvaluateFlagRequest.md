# EvaluateFlagRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | Pointer to **string** |  | [optional] 
**Context** | Pointer to **map[string]string** |  | [optional] 

## Methods

### NewEvaluateFlagRequest

`func NewEvaluateFlagRequest() *EvaluateFlagRequest`

NewEvaluateFlagRequest instantiates a new EvaluateFlagRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEvaluateFlagRequestWithDefaults

`func NewEvaluateFlagRequestWithDefaults() *EvaluateFlagRequest`

NewEvaluateFlagRequestWithDefaults instantiates a new EvaluateFlagRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKey

`func (o *EvaluateFlagRequest) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *EvaluateFlagRequest) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *EvaluateFlagRequest) SetKey(v string)`

SetKey sets Key field to given value.

### HasKey

`func (o *EvaluateFlagRequest) HasKey() bool`

HasKey returns a boolean if a field has been set.

### GetContext

`func (o *EvaluateFlagRequest) GetContext() map[string]string`

GetContext returns the Context field if non-nil, zero value otherwise.

### GetContextOk

`func (o *EvaluateFlagRequest) GetContextOk() (*map[string]string, bool)`

GetContextOk returns a tuple with the Context field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContext

`func (o *EvaluateFlagRequest) SetContext(v map[string]string)`

SetContext sets Context field to given value.

### HasContext

`func (o *EvaluateFlagRequest) HasContext() bool`

HasContext returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


