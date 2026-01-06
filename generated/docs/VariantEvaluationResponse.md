# VariantEvaluationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Match** | Pointer to **bool** |  | [optional] 
**SegmentKeys** | Pointer to **[]string** |  | [optional] 
**Reason** | Pointer to **string** |  | [optional] 
**VariantKey** | Pointer to **string** |  | [optional] 
**VariantAttachment** | Pointer to **string** |  | [optional] 
**RequestId** | Pointer to **string** |  | [optional] 
**RequestDurationMillis** | Pointer to **float64** |  | [optional] 
**Timestamp** | Pointer to **time.Time** |  | [optional] 
**FlagKey** | Pointer to **string** |  | [optional] 

## Methods

### NewVariantEvaluationResponse

`func NewVariantEvaluationResponse() *VariantEvaluationResponse`

NewVariantEvaluationResponse instantiates a new VariantEvaluationResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVariantEvaluationResponseWithDefaults

`func NewVariantEvaluationResponseWithDefaults() *VariantEvaluationResponse`

NewVariantEvaluationResponseWithDefaults instantiates a new VariantEvaluationResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMatch

`func (o *VariantEvaluationResponse) GetMatch() bool`

GetMatch returns the Match field if non-nil, zero value otherwise.

### GetMatchOk

`func (o *VariantEvaluationResponse) GetMatchOk() (*bool, bool)`

GetMatchOk returns a tuple with the Match field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatch

`func (o *VariantEvaluationResponse) SetMatch(v bool)`

SetMatch sets Match field to given value.

### HasMatch

`func (o *VariantEvaluationResponse) HasMatch() bool`

HasMatch returns a boolean if a field has been set.

### GetSegmentKeys

`func (o *VariantEvaluationResponse) GetSegmentKeys() []string`

GetSegmentKeys returns the SegmentKeys field if non-nil, zero value otherwise.

### GetSegmentKeysOk

`func (o *VariantEvaluationResponse) GetSegmentKeysOk() (*[]string, bool)`

GetSegmentKeysOk returns a tuple with the SegmentKeys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKeys

`func (o *VariantEvaluationResponse) SetSegmentKeys(v []string)`

SetSegmentKeys sets SegmentKeys field to given value.

### HasSegmentKeys

`func (o *VariantEvaluationResponse) HasSegmentKeys() bool`

HasSegmentKeys returns a boolean if a field has been set.

### GetReason

`func (o *VariantEvaluationResponse) GetReason() string`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *VariantEvaluationResponse) GetReasonOk() (*string, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *VariantEvaluationResponse) SetReason(v string)`

SetReason sets Reason field to given value.

### HasReason

`func (o *VariantEvaluationResponse) HasReason() bool`

HasReason returns a boolean if a field has been set.

### GetVariantKey

`func (o *VariantEvaluationResponse) GetVariantKey() string`

GetVariantKey returns the VariantKey field if non-nil, zero value otherwise.

### GetVariantKeyOk

`func (o *VariantEvaluationResponse) GetVariantKeyOk() (*string, bool)`

GetVariantKeyOk returns a tuple with the VariantKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariantKey

`func (o *VariantEvaluationResponse) SetVariantKey(v string)`

SetVariantKey sets VariantKey field to given value.

### HasVariantKey

`func (o *VariantEvaluationResponse) HasVariantKey() bool`

HasVariantKey returns a boolean if a field has been set.

### GetVariantAttachment

`func (o *VariantEvaluationResponse) GetVariantAttachment() string`

GetVariantAttachment returns the VariantAttachment field if non-nil, zero value otherwise.

### GetVariantAttachmentOk

`func (o *VariantEvaluationResponse) GetVariantAttachmentOk() (*string, bool)`

GetVariantAttachmentOk returns a tuple with the VariantAttachment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariantAttachment

`func (o *VariantEvaluationResponse) SetVariantAttachment(v string)`

SetVariantAttachment sets VariantAttachment field to given value.

### HasVariantAttachment

`func (o *VariantEvaluationResponse) HasVariantAttachment() bool`

HasVariantAttachment returns a boolean if a field has been set.

### GetRequestId

`func (o *VariantEvaluationResponse) GetRequestId() string`

GetRequestId returns the RequestId field if non-nil, zero value otherwise.

### GetRequestIdOk

`func (o *VariantEvaluationResponse) GetRequestIdOk() (*string, bool)`

GetRequestIdOk returns a tuple with the RequestId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestId

`func (o *VariantEvaluationResponse) SetRequestId(v string)`

SetRequestId sets RequestId field to given value.

### HasRequestId

`func (o *VariantEvaluationResponse) HasRequestId() bool`

HasRequestId returns a boolean if a field has been set.

### GetRequestDurationMillis

`func (o *VariantEvaluationResponse) GetRequestDurationMillis() float64`

GetRequestDurationMillis returns the RequestDurationMillis field if non-nil, zero value otherwise.

### GetRequestDurationMillisOk

`func (o *VariantEvaluationResponse) GetRequestDurationMillisOk() (*float64, bool)`

GetRequestDurationMillisOk returns a tuple with the RequestDurationMillis field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestDurationMillis

`func (o *VariantEvaluationResponse) SetRequestDurationMillis(v float64)`

SetRequestDurationMillis sets RequestDurationMillis field to given value.

### HasRequestDurationMillis

`func (o *VariantEvaluationResponse) HasRequestDurationMillis() bool`

HasRequestDurationMillis returns a boolean if a field has been set.

### GetTimestamp

`func (o *VariantEvaluationResponse) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *VariantEvaluationResponse) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *VariantEvaluationResponse) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.

### HasTimestamp

`func (o *VariantEvaluationResponse) HasTimestamp() bool`

HasTimestamp returns a boolean if a field has been set.

### GetFlagKey

`func (o *VariantEvaluationResponse) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *VariantEvaluationResponse) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *VariantEvaluationResponse) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *VariantEvaluationResponse) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


