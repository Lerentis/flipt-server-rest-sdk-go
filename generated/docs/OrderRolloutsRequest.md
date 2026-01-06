# OrderRolloutsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FlagKey** | Pointer to **string** |  | [optional] 
**NamespaceKey** | Pointer to **string** |  | [optional] 
**RolloutIds** | **[]string** |  | 

## Methods

### NewOrderRolloutsRequest

`func NewOrderRolloutsRequest(rolloutIds []string, ) *OrderRolloutsRequest`

NewOrderRolloutsRequest instantiates a new OrderRolloutsRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderRolloutsRequestWithDefaults

`func NewOrderRolloutsRequestWithDefaults() *OrderRolloutsRequest`

NewOrderRolloutsRequestWithDefaults instantiates a new OrderRolloutsRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFlagKey

`func (o *OrderRolloutsRequest) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *OrderRolloutsRequest) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *OrderRolloutsRequest) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *OrderRolloutsRequest) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.

### GetNamespaceKey

`func (o *OrderRolloutsRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *OrderRolloutsRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *OrderRolloutsRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *OrderRolloutsRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetRolloutIds

`func (o *OrderRolloutsRequest) GetRolloutIds() []string`

GetRolloutIds returns the RolloutIds field if non-nil, zero value otherwise.

### GetRolloutIdsOk

`func (o *OrderRolloutsRequest) GetRolloutIdsOk() (*[]string, bool)`

GetRolloutIdsOk returns a tuple with the RolloutIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRolloutIds

`func (o *OrderRolloutsRequest) SetRolloutIds(v []string)`

SetRolloutIds sets RolloutIds field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


