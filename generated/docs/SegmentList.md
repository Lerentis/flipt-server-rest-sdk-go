# SegmentList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Segments** | Pointer to [**[]Segment**](Segment.md) |  | [optional] 
**NextPageToken** | Pointer to **string** |  | [optional] 
**TotalCount** | Pointer to **int32** |  | [optional] 

## Methods

### NewSegmentList

`func NewSegmentList() *SegmentList`

NewSegmentList instantiates a new SegmentList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSegmentListWithDefaults

`func NewSegmentListWithDefaults() *SegmentList`

NewSegmentListWithDefaults instantiates a new SegmentList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSegments

`func (o *SegmentList) GetSegments() []Segment`

GetSegments returns the Segments field if non-nil, zero value otherwise.

### GetSegmentsOk

`func (o *SegmentList) GetSegmentsOk() (*[]Segment, bool)`

GetSegmentsOk returns a tuple with the Segments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegments

`func (o *SegmentList) SetSegments(v []Segment)`

SetSegments sets Segments field to given value.

### HasSegments

`func (o *SegmentList) HasSegments() bool`

HasSegments returns a boolean if a field has been set.

### GetNextPageToken

`func (o *SegmentList) GetNextPageToken() string`

GetNextPageToken returns the NextPageToken field if non-nil, zero value otherwise.

### GetNextPageTokenOk

`func (o *SegmentList) GetNextPageTokenOk() (*string, bool)`

GetNextPageTokenOk returns a tuple with the NextPageToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextPageToken

`func (o *SegmentList) SetNextPageToken(v string)`

SetNextPageToken sets NextPageToken field to given value.

### HasNextPageToken

`func (o *SegmentList) HasNextPageToken() bool`

HasNextPageToken returns a boolean if a field has been set.

### GetTotalCount

`func (o *SegmentList) GetTotalCount() int32`

GetTotalCount returns the TotalCount field if non-nil, zero value otherwise.

### GetTotalCountOk

`func (o *SegmentList) GetTotalCountOk() (*int32, bool)`

GetTotalCountOk returns a tuple with the TotalCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalCount

`func (o *SegmentList) SetTotalCount(v int32)`

SetTotalCount sets TotalCount field to given value.

### HasTotalCount

`func (o *SegmentList) HasTotalCount() bool`

HasTotalCount returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


