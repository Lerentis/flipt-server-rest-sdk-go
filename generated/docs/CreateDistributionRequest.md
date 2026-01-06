# CreateDistributionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FlagKey** | Pointer to **string** |  | [optional] 
**RuleId** | Pointer to **string** |  | [optional] 
**VariantId** | **string** |  | 
**Rollout** | **float32** |  | 
**NamespaceKey** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateDistributionRequest

`func NewCreateDistributionRequest(variantId string, rollout float32, ) *CreateDistributionRequest`

NewCreateDistributionRequest instantiates a new CreateDistributionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateDistributionRequestWithDefaults

`func NewCreateDistributionRequestWithDefaults() *CreateDistributionRequest`

NewCreateDistributionRequestWithDefaults instantiates a new CreateDistributionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFlagKey

`func (o *CreateDistributionRequest) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *CreateDistributionRequest) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *CreateDistributionRequest) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *CreateDistributionRequest) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.

### GetRuleId

`func (o *CreateDistributionRequest) GetRuleId() string`

GetRuleId returns the RuleId field if non-nil, zero value otherwise.

### GetRuleIdOk

`func (o *CreateDistributionRequest) GetRuleIdOk() (*string, bool)`

GetRuleIdOk returns a tuple with the RuleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRuleId

`func (o *CreateDistributionRequest) SetRuleId(v string)`

SetRuleId sets RuleId field to given value.

### HasRuleId

`func (o *CreateDistributionRequest) HasRuleId() bool`

HasRuleId returns a boolean if a field has been set.

### GetVariantId

`func (o *CreateDistributionRequest) GetVariantId() string`

GetVariantId returns the VariantId field if non-nil, zero value otherwise.

### GetVariantIdOk

`func (o *CreateDistributionRequest) GetVariantIdOk() (*string, bool)`

GetVariantIdOk returns a tuple with the VariantId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariantId

`func (o *CreateDistributionRequest) SetVariantId(v string)`

SetVariantId sets VariantId field to given value.


### GetRollout

`func (o *CreateDistributionRequest) GetRollout() float32`

GetRollout returns the Rollout field if non-nil, zero value otherwise.

### GetRolloutOk

`func (o *CreateDistributionRequest) GetRolloutOk() (*float32, bool)`

GetRolloutOk returns a tuple with the Rollout field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRollout

`func (o *CreateDistributionRequest) SetRollout(v float32)`

SetRollout sets Rollout field to given value.


### GetNamespaceKey

`func (o *CreateDistributionRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *CreateDistributionRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *CreateDistributionRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *CreateDistributionRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


