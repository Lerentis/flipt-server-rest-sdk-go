# RolloutList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Rules** | Pointer to [**[]Rollout**](Rollout.md) |  | [optional] 
**NextPageToken** | Pointer to **string** |  | [optional] 
**TotalCount** | Pointer to **int32** |  | [optional] 

## Methods

### NewRolloutList

`func NewRolloutList() *RolloutList`

NewRolloutList instantiates a new RolloutList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRolloutListWithDefaults

`func NewRolloutListWithDefaults() *RolloutList`

NewRolloutListWithDefaults instantiates a new RolloutList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRules

`func (o *RolloutList) GetRules() []Rollout`

GetRules returns the Rules field if non-nil, zero value otherwise.

### GetRulesOk

`func (o *RolloutList) GetRulesOk() (*[]Rollout, bool)`

GetRulesOk returns a tuple with the Rules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRules

`func (o *RolloutList) SetRules(v []Rollout)`

SetRules sets Rules field to given value.

### HasRules

`func (o *RolloutList) HasRules() bool`

HasRules returns a boolean if a field has been set.

### GetNextPageToken

`func (o *RolloutList) GetNextPageToken() string`

GetNextPageToken returns the NextPageToken field if non-nil, zero value otherwise.

### GetNextPageTokenOk

`func (o *RolloutList) GetNextPageTokenOk() (*string, bool)`

GetNextPageTokenOk returns a tuple with the NextPageToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextPageToken

`func (o *RolloutList) SetNextPageToken(v string)`

SetNextPageToken sets NextPageToken field to given value.

### HasNextPageToken

`func (o *RolloutList) HasNextPageToken() bool`

HasNextPageToken returns a boolean if a field has been set.

### GetTotalCount

`func (o *RolloutList) GetTotalCount() int32`

GetTotalCount returns the TotalCount field if non-nil, zero value otherwise.

### GetTotalCountOk

`func (o *RolloutList) GetTotalCountOk() (*int32, bool)`

GetTotalCountOk returns a tuple with the TotalCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalCount

`func (o *RolloutList) SetTotalCount(v int32)`

SetTotalCount sets TotalCount field to given value.

### HasTotalCount

`func (o *RolloutList) HasTotalCount() bool`

HasTotalCount returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


