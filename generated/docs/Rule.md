# Rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**FlagKey** | Pointer to **string** |  | [optional] 
**SegmentKey** | Pointer to **string** |  | [optional] 
**Distributions** | Pointer to [**[]Distribution**](Distribution.md) |  | [optional] 
**Rank** | Pointer to **int32** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**NamespaceKey** | Pointer to **string** |  | [optional] 
**SegmentKeys** | Pointer to **[]string** |  | [optional] 
**SegmentOperator** | Pointer to **string** |  | [optional] 

## Methods

### NewRule

`func NewRule() *Rule`

NewRule instantiates a new Rule object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRuleWithDefaults

`func NewRuleWithDefaults() *Rule`

NewRuleWithDefaults instantiates a new Rule object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Rule) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Rule) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Rule) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *Rule) HasId() bool`

HasId returns a boolean if a field has been set.

### GetFlagKey

`func (o *Rule) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *Rule) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *Rule) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *Rule) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.

### GetSegmentKey

`func (o *Rule) GetSegmentKey() string`

GetSegmentKey returns the SegmentKey field if non-nil, zero value otherwise.

### GetSegmentKeyOk

`func (o *Rule) GetSegmentKeyOk() (*string, bool)`

GetSegmentKeyOk returns a tuple with the SegmentKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKey

`func (o *Rule) SetSegmentKey(v string)`

SetSegmentKey sets SegmentKey field to given value.

### HasSegmentKey

`func (o *Rule) HasSegmentKey() bool`

HasSegmentKey returns a boolean if a field has been set.

### GetDistributions

`func (o *Rule) GetDistributions() []Distribution`

GetDistributions returns the Distributions field if non-nil, zero value otherwise.

### GetDistributionsOk

`func (o *Rule) GetDistributionsOk() (*[]Distribution, bool)`

GetDistributionsOk returns a tuple with the Distributions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDistributions

`func (o *Rule) SetDistributions(v []Distribution)`

SetDistributions sets Distributions field to given value.

### HasDistributions

`func (o *Rule) HasDistributions() bool`

HasDistributions returns a boolean if a field has been set.

### GetRank

`func (o *Rule) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *Rule) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *Rule) SetRank(v int32)`

SetRank sets Rank field to given value.

### HasRank

`func (o *Rule) HasRank() bool`

HasRank returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Rule) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Rule) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Rule) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Rule) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *Rule) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Rule) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Rule) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *Rule) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetNamespaceKey

`func (o *Rule) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *Rule) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *Rule) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *Rule) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetSegmentKeys

`func (o *Rule) GetSegmentKeys() []string`

GetSegmentKeys returns the SegmentKeys field if non-nil, zero value otherwise.

### GetSegmentKeysOk

`func (o *Rule) GetSegmentKeysOk() (*[]string, bool)`

GetSegmentKeysOk returns a tuple with the SegmentKeys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKeys

`func (o *Rule) SetSegmentKeys(v []string)`

SetSegmentKeys sets SegmentKeys field to given value.

### HasSegmentKeys

`func (o *Rule) HasSegmentKeys() bool`

HasSegmentKeys returns a boolean if a field has been set.

### GetSegmentOperator

`func (o *Rule) GetSegmentOperator() string`

GetSegmentOperator returns the SegmentOperator field if non-nil, zero value otherwise.

### GetSegmentOperatorOk

`func (o *Rule) GetSegmentOperatorOk() (*string, bool)`

GetSegmentOperatorOk returns a tuple with the SegmentOperator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentOperator

`func (o *Rule) SetSegmentOperator(v string)`

SetSegmentOperator sets SegmentOperator field to given value.

### HasSegmentOperator

`func (o *Rule) HasSegmentOperator() bool`

HasSegmentOperator returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


