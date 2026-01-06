# UpdateDistributionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**FlagKey** | Pointer to **string** |  | [optional] 
**RuleId** | Pointer to **string** |  | [optional] 
**VariantId** | **string** |  | 
**Rollout** | **float32** |  | 
**NamespaceKey** | Pointer to **string** |  | [optional] 

## Methods

### NewUpdateDistributionRequest

`func NewUpdateDistributionRequest(variantId string, rollout float32, ) *UpdateDistributionRequest`

NewUpdateDistributionRequest instantiates a new UpdateDistributionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateDistributionRequestWithDefaults

`func NewUpdateDistributionRequestWithDefaults() *UpdateDistributionRequest`

NewUpdateDistributionRequestWithDefaults instantiates a new UpdateDistributionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpdateDistributionRequest) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateDistributionRequest) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateDistributionRequest) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *UpdateDistributionRequest) HasId() bool`

HasId returns a boolean if a field has been set.

### GetFlagKey

`func (o *UpdateDistributionRequest) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *UpdateDistributionRequest) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *UpdateDistributionRequest) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *UpdateDistributionRequest) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.

### GetRuleId

`func (o *UpdateDistributionRequest) GetRuleId() string`

GetRuleId returns the RuleId field if non-nil, zero value otherwise.

### GetRuleIdOk

`func (o *UpdateDistributionRequest) GetRuleIdOk() (*string, bool)`

GetRuleIdOk returns a tuple with the RuleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRuleId

`func (o *UpdateDistributionRequest) SetRuleId(v string)`

SetRuleId sets RuleId field to given value.

### HasRuleId

`func (o *UpdateDistributionRequest) HasRuleId() bool`

HasRuleId returns a boolean if a field has been set.

### GetVariantId

`func (o *UpdateDistributionRequest) GetVariantId() string`

GetVariantId returns the VariantId field if non-nil, zero value otherwise.

### GetVariantIdOk

`func (o *UpdateDistributionRequest) GetVariantIdOk() (*string, bool)`

GetVariantIdOk returns a tuple with the VariantId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariantId

`func (o *UpdateDistributionRequest) SetVariantId(v string)`

SetVariantId sets VariantId field to given value.


### GetRollout

`func (o *UpdateDistributionRequest) GetRollout() float32`

GetRollout returns the Rollout field if non-nil, zero value otherwise.

### GetRolloutOk

`func (o *UpdateDistributionRequest) GetRolloutOk() (*float32, bool)`

GetRolloutOk returns a tuple with the Rollout field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRollout

`func (o *UpdateDistributionRequest) SetRollout(v float32)`

SetRollout sets Rollout field to given value.


### GetNamespaceKey

`func (o *UpdateDistributionRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *UpdateDistributionRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *UpdateDistributionRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *UpdateDistributionRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


