# OrderRulesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FlagKey** | Pointer to **string** |  | [optional] 
**RuleIds** | **[]string** |  | 
**NamespaceKey** | Pointer to **string** |  | [optional] 

## Methods

### NewOrderRulesRequest

`func NewOrderRulesRequest(ruleIds []string, ) *OrderRulesRequest`

NewOrderRulesRequest instantiates a new OrderRulesRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOrderRulesRequestWithDefaults

`func NewOrderRulesRequestWithDefaults() *OrderRulesRequest`

NewOrderRulesRequestWithDefaults instantiates a new OrderRulesRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFlagKey

`func (o *OrderRulesRequest) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *OrderRulesRequest) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *OrderRulesRequest) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *OrderRulesRequest) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.

### GetRuleIds

`func (o *OrderRulesRequest) GetRuleIds() []string`

GetRuleIds returns the RuleIds field if non-nil, zero value otherwise.

### GetRuleIdsOk

`func (o *OrderRulesRequest) GetRuleIdsOk() (*[]string, bool)`

GetRuleIdsOk returns a tuple with the RuleIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRuleIds

`func (o *OrderRulesRequest) SetRuleIds(v []string)`

SetRuleIds sets RuleIds field to given value.


### GetNamespaceKey

`func (o *OrderRulesRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *OrderRulesRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *OrderRulesRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *OrderRulesRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


