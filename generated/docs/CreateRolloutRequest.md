# CreateRolloutRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**NamespaceKey** | Pointer to **string** |  | [optional] 
**FlagKey** | Pointer to **string** |  | [optional] 
**Rank** | **int32** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Segment** | Pointer to [**RolloutSegment**](RolloutSegment.md) |  | [optional] 
**Threshold** | Pointer to [**RolloutThreshold**](RolloutThreshold.md) |  | [optional] 

## Methods

### NewCreateRolloutRequest

`func NewCreateRolloutRequest(rank int32, ) *CreateRolloutRequest`

NewCreateRolloutRequest instantiates a new CreateRolloutRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateRolloutRequestWithDefaults

`func NewCreateRolloutRequestWithDefaults() *CreateRolloutRequest`

NewCreateRolloutRequestWithDefaults instantiates a new CreateRolloutRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetNamespaceKey

`func (o *CreateRolloutRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *CreateRolloutRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *CreateRolloutRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *CreateRolloutRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetFlagKey

`func (o *CreateRolloutRequest) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *CreateRolloutRequest) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *CreateRolloutRequest) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *CreateRolloutRequest) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.

### GetRank

`func (o *CreateRolloutRequest) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *CreateRolloutRequest) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *CreateRolloutRequest) SetRank(v int32)`

SetRank sets Rank field to given value.


### GetDescription

`func (o *CreateRolloutRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateRolloutRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateRolloutRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateRolloutRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetSegment

`func (o *CreateRolloutRequest) GetSegment() RolloutSegment`

GetSegment returns the Segment field if non-nil, zero value otherwise.

### GetSegmentOk

`func (o *CreateRolloutRequest) GetSegmentOk() (*RolloutSegment, bool)`

GetSegmentOk returns a tuple with the Segment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegment

`func (o *CreateRolloutRequest) SetSegment(v RolloutSegment)`

SetSegment sets Segment field to given value.

### HasSegment

`func (o *CreateRolloutRequest) HasSegment() bool`

HasSegment returns a boolean if a field has been set.

### GetThreshold

`func (o *CreateRolloutRequest) GetThreshold() RolloutThreshold`

GetThreshold returns the Threshold field if non-nil, zero value otherwise.

### GetThresholdOk

`func (o *CreateRolloutRequest) GetThresholdOk() (*RolloutThreshold, bool)`

GetThresholdOk returns a tuple with the Threshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreshold

`func (o *CreateRolloutRequest) SetThreshold(v RolloutThreshold)`

SetThreshold sets Threshold field to given value.

### HasThreshold

`func (o *CreateRolloutRequest) HasThreshold() bool`

HasThreshold returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


