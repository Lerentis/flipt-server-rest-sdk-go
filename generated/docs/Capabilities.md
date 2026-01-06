# Capabilities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CacheInvalidation** | Pointer to [**CacheInvalidation**](CacheInvalidation.md) |  | [optional] 
**FlagEvaluation** | Pointer to [**FlagEvaluation**](FlagEvaluation.md) |  | [optional] 

## Methods

### NewCapabilities

`func NewCapabilities() *Capabilities`

NewCapabilities instantiates a new Capabilities object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCapabilitiesWithDefaults

`func NewCapabilitiesWithDefaults() *Capabilities`

NewCapabilitiesWithDefaults instantiates a new Capabilities object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCacheInvalidation

`func (o *Capabilities) GetCacheInvalidation() CacheInvalidation`

GetCacheInvalidation returns the CacheInvalidation field if non-nil, zero value otherwise.

### GetCacheInvalidationOk

`func (o *Capabilities) GetCacheInvalidationOk() (*CacheInvalidation, bool)`

GetCacheInvalidationOk returns a tuple with the CacheInvalidation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCacheInvalidation

`func (o *Capabilities) SetCacheInvalidation(v CacheInvalidation)`

SetCacheInvalidation sets CacheInvalidation field to given value.

### HasCacheInvalidation

`func (o *Capabilities) HasCacheInvalidation() bool`

HasCacheInvalidation returns a boolean if a field has been set.

### GetFlagEvaluation

`func (o *Capabilities) GetFlagEvaluation() FlagEvaluation`

GetFlagEvaluation returns the FlagEvaluation field if non-nil, zero value otherwise.

### GetFlagEvaluationOk

`func (o *Capabilities) GetFlagEvaluationOk() (*FlagEvaluation, bool)`

GetFlagEvaluationOk returns a tuple with the FlagEvaluation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagEvaluation

`func (o *Capabilities) SetFlagEvaluation(v FlagEvaluation)`

SetFlagEvaluation sets FlagEvaluation field to given value.

### HasFlagEvaluation

`func (o *Capabilities) HasFlagEvaluation() bool`

HasFlagEvaluation returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


