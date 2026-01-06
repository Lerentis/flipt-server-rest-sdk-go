# FlagList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Flags** | Pointer to [**[]Flag**](Flag.md) |  | [optional] 
**NextPageToken** | Pointer to **string** |  | [optional] 
**TotalCount** | Pointer to **int32** |  | [optional] 

## Methods

### NewFlagList

`func NewFlagList() *FlagList`

NewFlagList instantiates a new FlagList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlagListWithDefaults

`func NewFlagListWithDefaults() *FlagList`

NewFlagListWithDefaults instantiates a new FlagList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFlags

`func (o *FlagList) GetFlags() []Flag`

GetFlags returns the Flags field if non-nil, zero value otherwise.

### GetFlagsOk

`func (o *FlagList) GetFlagsOk() (*[]Flag, bool)`

GetFlagsOk returns a tuple with the Flags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlags

`func (o *FlagList) SetFlags(v []Flag)`

SetFlags sets Flags field to given value.

### HasFlags

`func (o *FlagList) HasFlags() bool`

HasFlags returns a boolean if a field has been set.

### GetNextPageToken

`func (o *FlagList) GetNextPageToken() string`

GetNextPageToken returns the NextPageToken field if non-nil, zero value otherwise.

### GetNextPageTokenOk

`func (o *FlagList) GetNextPageTokenOk() (*string, bool)`

GetNextPageTokenOk returns a tuple with the NextPageToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextPageToken

`func (o *FlagList) SetNextPageToken(v string)`

SetNextPageToken sets NextPageToken field to given value.

### HasNextPageToken

`func (o *FlagList) HasNextPageToken() bool`

HasNextPageToken returns a boolean if a field has been set.

### GetTotalCount

`func (o *FlagList) GetTotalCount() int32`

GetTotalCount returns the TotalCount field if non-nil, zero value otherwise.

### GetTotalCountOk

`func (o *FlagList) GetTotalCountOk() (*int32, bool)`

GetTotalCountOk returns a tuple with the TotalCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalCount

`func (o *FlagList) SetTotalCount(v int32)`

SetTotalCount sets TotalCount field to given value.

### HasTotalCount

`func (o *FlagList) HasTotalCount() bool`

HasTotalCount returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


