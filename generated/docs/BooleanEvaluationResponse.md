# BooleanEvaluationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | Pointer to **bool** |  | [optional] 
**Reason** | Pointer to **string** |  | [optional] 
**RequestId** | Pointer to **string** |  | [optional] 
**RequestDurationMillis** | Pointer to **float64** |  | [optional] 
**Timestamp** | Pointer to **time.Time** |  | [optional] 
**FlagKey** | Pointer to **string** |  | [optional] 
**SegmentKeys** | Pointer to **[]string** |  | [optional] 

## Methods

### NewBooleanEvaluationResponse

`func NewBooleanEvaluationResponse() *BooleanEvaluationResponse`

NewBooleanEvaluationResponse instantiates a new BooleanEvaluationResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBooleanEvaluationResponseWithDefaults

`func NewBooleanEvaluationResponseWithDefaults() *BooleanEvaluationResponse`

NewBooleanEvaluationResponseWithDefaults instantiates a new BooleanEvaluationResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *BooleanEvaluationResponse) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *BooleanEvaluationResponse) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *BooleanEvaluationResponse) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *BooleanEvaluationResponse) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetReason

`func (o *BooleanEvaluationResponse) GetReason() string`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *BooleanEvaluationResponse) GetReasonOk() (*string, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *BooleanEvaluationResponse) SetReason(v string)`

SetReason sets Reason field to given value.

### HasReason

`func (o *BooleanEvaluationResponse) HasReason() bool`

HasReason returns a boolean if a field has been set.

### GetRequestId

`func (o *BooleanEvaluationResponse) GetRequestId() string`

GetRequestId returns the RequestId field if non-nil, zero value otherwise.

### GetRequestIdOk

`func (o *BooleanEvaluationResponse) GetRequestIdOk() (*string, bool)`

GetRequestIdOk returns a tuple with the RequestId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestId

`func (o *BooleanEvaluationResponse) SetRequestId(v string)`

SetRequestId sets RequestId field to given value.

### HasRequestId

`func (o *BooleanEvaluationResponse) HasRequestId() bool`

HasRequestId returns a boolean if a field has been set.

### GetRequestDurationMillis

`func (o *BooleanEvaluationResponse) GetRequestDurationMillis() float64`

GetRequestDurationMillis returns the RequestDurationMillis field if non-nil, zero value otherwise.

### GetRequestDurationMillisOk

`func (o *BooleanEvaluationResponse) GetRequestDurationMillisOk() (*float64, bool)`

GetRequestDurationMillisOk returns a tuple with the RequestDurationMillis field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestDurationMillis

`func (o *BooleanEvaluationResponse) SetRequestDurationMillis(v float64)`

SetRequestDurationMillis sets RequestDurationMillis field to given value.

### HasRequestDurationMillis

`func (o *BooleanEvaluationResponse) HasRequestDurationMillis() bool`

HasRequestDurationMillis returns a boolean if a field has been set.

### GetTimestamp

`func (o *BooleanEvaluationResponse) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *BooleanEvaluationResponse) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *BooleanEvaluationResponse) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.

### HasTimestamp

`func (o *BooleanEvaluationResponse) HasTimestamp() bool`

HasTimestamp returns a boolean if a field has been set.

### GetFlagKey

`func (o *BooleanEvaluationResponse) GetFlagKey() string`

GetFlagKey returns the FlagKey field if non-nil, zero value otherwise.

### GetFlagKeyOk

`func (o *BooleanEvaluationResponse) GetFlagKeyOk() (*string, bool)`

GetFlagKeyOk returns a tuple with the FlagKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFlagKey

`func (o *BooleanEvaluationResponse) SetFlagKey(v string)`

SetFlagKey sets FlagKey field to given value.

### HasFlagKey

`func (o *BooleanEvaluationResponse) HasFlagKey() bool`

HasFlagKey returns a boolean if a field has been set.

### GetSegmentKeys

`func (o *BooleanEvaluationResponse) GetSegmentKeys() []string`

GetSegmentKeys returns the SegmentKeys field if non-nil, zero value otherwise.

### GetSegmentKeysOk

`func (o *BooleanEvaluationResponse) GetSegmentKeysOk() (*[]string, bool)`

GetSegmentKeysOk returns a tuple with the SegmentKeys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKeys

`func (o *BooleanEvaluationResponse) SetSegmentKeys(v []string)`

SetSegmentKeys sets SegmentKeys field to given value.

### HasSegmentKeys

`func (o *BooleanEvaluationResponse) HasSegmentKeys() bool`

HasSegmentKeys returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


