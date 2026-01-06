# UpdateRolloutRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**NamespaceKey** | Pointer to **string** |  | [optional] 
**FlagKey** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Segment** | Pointer to [**RolloutSegment**](RolloutSegment.md) |  | [optional] 
**Threshold** | Pointer to [**RolloutThreshold**](RolloutThreshold.md) |  | [optional] 

## Methods

### NewUpdateRolloutRequest

`func NewUpdateRolloutRequest() *UpdateRolloutRequest`

NewUpdateRolloutRequest instantiates a new UpdateRolloutRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateRolloutRequestWithDefaults

`func NewUpdateRolloutRequestWithDefaults() *UpdateRolloutRequest`

NewUpdateRolloutRequestWithDefaults instantiates a new UpdateRolloutRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpdateRolloutRequest) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateRolloutRequest) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateRolloutRequest) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *UpdateRolloutRequest) HasId() bool`

HasId returns a boolean if a field has been set.

### GetNamespaceKey

`func (o *UpdateRolloutRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *UpdateRolloutRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *UpdateRolloutRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *UpdateRolloutRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetFlagKey

`func (o *UpdateRolloutRequest) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *UpdateRolloutRequest) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *UpdateRolloutRequest) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *UpdateRolloutRequest) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.

### GetDescription

`func (o *UpdateRolloutRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *UpdateRolloutRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *UpdateRolloutRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *UpdateRolloutRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetSegment

`func (o *UpdateRolloutRequest) GetSegment() RolloutSegment`

GetSegment returns the Segment field if non-nil, zero value otherwise.

### GetSegmentOk

`func (o *UpdateRolloutRequest) GetSegmentOk() (*RolloutSegment, bool)`

GetSegmentOk returns a tuple with the Segment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegment

`func (o *UpdateRolloutRequest) SetSegment(v RolloutSegment)`

SetSegment sets Segment field to given value.

### HasSegment

`func (o *UpdateRolloutRequest) HasSegment() bool`

HasSegment returns a boolean if a field has been set.

### GetThreshold

`func (o *UpdateRolloutRequest) GetThreshold() RolloutThreshold`

GetThreshold returns the Threshold field if non-nil, zero value otherwise.

### GetThresholdOk

`func (o *UpdateRolloutRequest) GetThresholdOk() (*RolloutThreshold, bool)`

GetThresholdOk returns a tuple with the Threshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreshold

`func (o *UpdateRolloutRequest) SetThreshold(v RolloutThreshold)`

SetThreshold sets Threshold field to given value.

### HasThreshold

`func (o *UpdateRolloutRequest) HasThreshold() bool`

HasThreshold returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


