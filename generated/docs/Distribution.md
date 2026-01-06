# Distribution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**RuleId** | Pointer to **string** |  | [optional] 
**VariantId** | Pointer to **string** |  | [optional] 
**Rollout** | Pointer to **float32** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewDistribution

`func NewDistribution() *Distribution`

NewDistribution instantiates a new Distribution object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDistributionWithDefaults

`func NewDistributionWithDefaults() *Distribution`

NewDistributionWithDefaults instantiates a new Distribution object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Distribution) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Distribution) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Distribution) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *Distribution) HasId() bool`

HasId returns a boolean if a field has been set.

### GetRuleId

`func (o *Distribution) GetRuleId() string`

GetRuleId returns the RuleId field if non-nil, zero value otherwise.

### GetRuleIdOk

`func (o *Distribution) GetRuleIdOk() (*string, bool)`

GetRuleIdOk returns a tuple with the RuleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRuleId

`func (o *Distribution) SetRuleId(v string)`

SetRuleId sets RuleId field to given value.

### HasRuleId

`func (o *Distribution) HasRuleId() bool`

HasRuleId returns a boolean if a field has been set.

### GetVariantId

`func (o *Distribution) GetVariantId() string`

GetVariantId returns the VariantId field if non-nil, zero value otherwise.

### GetVariantIdOk

`func (o *Distribution) GetVariantIdOk() (*string, bool)`

GetVariantIdOk returns a tuple with the VariantId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariantId

`func (o *Distribution) SetVariantId(v string)`

SetVariantId sets VariantId field to given value.

### HasVariantId

`func (o *Distribution) HasVariantId() bool`

HasVariantId returns a boolean if a field has been set.

### GetRollout

`func (o *Distribution) GetRollout() float32`

GetRollout returns the Rollout field if non-nil, zero value otherwise.

### GetRolloutOk

`func (o *Distribution) GetRolloutOk() (*float32, bool)`

GetRolloutOk returns a tuple with the Rollout field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRollout

`func (o *Distribution) SetRollout(v float32)`

SetRollout sets Rollout field to given value.

### HasRollout

`func (o *Distribution) HasRollout() bool`

HasRollout returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Distribution) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Distribution) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Distribution) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Distribution) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *Distribution) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Distribution) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Distribution) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *Distribution) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


