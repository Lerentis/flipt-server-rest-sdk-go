# CreateRuleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FlagKey** | Pointer to **string** |  | [optional] 
**SegmentKey** | Pointer to **string** |  | [optional] 
**Rank** | **int32** |  | 
**NamespaceKey** | Pointer to **string** |  | [optional] 
**SegmentKeys** | Pointer to **[]string** |  | [optional] 
**SegmentOperator** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateRuleRequest

`func NewCreateRuleRequest(rank int32, ) *CreateRuleRequest`

NewCreateRuleRequest instantiates a new CreateRuleRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateRuleRequestWithDefaults

`func NewCreateRuleRequestWithDefaults() *CreateRuleRequest`

NewCreateRuleRequestWithDefaults instantiates a new CreateRuleRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFlagKey

`func (o *CreateRuleRequest) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *CreateRuleRequest) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *CreateRuleRequest) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *CreateRuleRequest) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.

### GetSegmentKey

`func (o *CreateRuleRequest) GetSegmentKey() string`

GetSegmentKey returns the SegmentKey field if non-nil, zero value otherwise.

### GetSegmentKeyOk

`func (o *CreateRuleRequest) GetSegmentKeyOk() (*string, bool)`

GetSegmentKeyOk returns a tuple with the SegmentKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKey

`func (o *CreateRuleRequest) SetSegmentKey(v string)`

SetSegmentKey sets SegmentKey field to given value.

### HasSegmentKey

`func (o *CreateRuleRequest) HasSegmentKey() bool`

HasSegmentKey returns a boolean if a field has been set.

### GetRank

`func (o *CreateRuleRequest) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *CreateRuleRequest) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *CreateRuleRequest) SetRank(v int32)`

SetRank sets Rank field to given value.


### GetNamespaceKey

`func (o *CreateRuleRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *CreateRuleRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *CreateRuleRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *CreateRuleRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetSegmentKeys

`func (o *CreateRuleRequest) GetSegmentKeys() []string`

GetSegmentKeys returns the SegmentKeys field if non-nil, zero value otherwise.

### GetSegmentKeysOk

`func (o *CreateRuleRequest) GetSegmentKeysOk() (*[]string, bool)`

GetSegmentKeysOk returns a tuple with the SegmentKeys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKeys

`func (o *CreateRuleRequest) SetSegmentKeys(v []string)`

SetSegmentKeys sets SegmentKeys field to given value.

### HasSegmentKeys

`func (o *CreateRuleRequest) HasSegmentKeys() bool`

HasSegmentKeys returns a boolean if a field has been set.

### GetSegmentOperator

`func (o *CreateRuleRequest) GetSegmentOperator() string`

GetSegmentOperator returns the SegmentOperator field if non-nil, zero value otherwise.

### GetSegmentOperatorOk

`func (o *CreateRuleRequest) GetSegmentOperatorOk() (*string, bool)`

GetSegmentOperatorOk returns a tuple with the SegmentOperator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentOperator

`func (o *CreateRuleRequest) SetSegmentOperator(v string)`

SetSegmentOperator sets SegmentOperator field to given value.

### HasSegmentOperator

`func (o *CreateRuleRequest) HasSegmentOperator() bool`

HasSegmentOperator returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


