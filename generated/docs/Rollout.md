# Rollout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**NamespaceKey** | Pointer to **string** |  | [optional] 
**FlagKey** | Pointer to **string** |  | [optional] 
**Type** | Pointer to **string** |  | [optional] 
**Rank** | Pointer to **int32** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**Segment** | Pointer to [**RolloutSegment**](RolloutSegment.md) |  | [optional] 
**Threshold** | Pointer to [**RolloutThreshold**](RolloutThreshold.md) |  | [optional] 

## Methods

### NewRollout

`func NewRollout() *Rollout`

NewRollout instantiates a new Rollout object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRolloutWithDefaults

`func NewRolloutWithDefaults() *Rollout`

NewRolloutWithDefaults instantiates a new Rollout object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Rollout) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Rollout) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Rollout) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *Rollout) HasId() bool`

HasId returns a boolean if a field has been set.

### GetNamespaceKey

`func (o *Rollout) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *Rollout) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *Rollout) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *Rollout) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetFlagKey

`func (o *Rollout) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *Rollout) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *Rollout) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *Rollout) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.

### GetType

`func (o *Rollout) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Rollout) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Rollout) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *Rollout) HasType() bool`

HasType returns a boolean if a field has been set.

### GetRank

`func (o *Rollout) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *Rollout) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *Rollout) SetRank(v int32)`

SetRank sets Rank field to given value.

### HasRank

`func (o *Rollout) HasRank() bool`

HasRank returns a boolean if a field has been set.

### GetDescription

`func (o *Rollout) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Rollout) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Rollout) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Rollout) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Rollout) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Rollout) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Rollout) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Rollout) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *Rollout) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Rollout) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Rollout) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *Rollout) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetSegment

`func (o *Rollout) GetSegment() RolloutSegment`

GetSegment returns the Segment field if non-nil, zero value otherwise.

### GetSegmentOk

`func (o *Rollout) GetSegmentOk() (*RolloutSegment, bool)`

GetSegmentOk returns a tuple with the Segment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegment

`func (o *Rollout) SetSegment(v RolloutSegment)`

SetSegment sets Segment field to given value.

### HasSegment

`func (o *Rollout) HasSegment() bool`

HasSegment returns a boolean if a field has been set.

### GetThreshold

`func (o *Rollout) GetThreshold() RolloutThreshold`

GetThreshold returns the Threshold field if non-nil, zero value otherwise.

### GetThresholdOk

`func (o *Rollout) GetThresholdOk() (*RolloutThreshold, bool)`

GetThresholdOk returns a tuple with the Threshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreshold

`func (o *Rollout) SetThreshold(v RolloutThreshold)`

SetThreshold sets Threshold field to given value.

### HasThreshold

`func (o *Rollout) HasThreshold() bool`

HasThreshold returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


