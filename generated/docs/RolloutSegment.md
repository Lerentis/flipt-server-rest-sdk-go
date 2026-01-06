# RolloutSegment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SegmentKey** | Pointer to **string** |  | [optional] 
**Value** | Pointer to **bool** |  | [optional] 
**SegmentKeys** | Pointer to **[]string** |  | [optional] 
**SegmentOperator** | Pointer to **string** |  | [optional] 

## Methods

### NewRolloutSegment

`func NewRolloutSegment() *RolloutSegment`

NewRolloutSegment instantiates a new RolloutSegment object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRolloutSegmentWithDefaults

`func NewRolloutSegmentWithDefaults() *RolloutSegment`

NewRolloutSegmentWithDefaults instantiates a new RolloutSegment object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSegmentKey

`func (o *RolloutSegment) GetSegmentKey() string`

GetSegmentKey returns the SegmentKey field if non-nil, zero value otherwise.

### GetSegmentKeyOk

`func (o *RolloutSegment) GetSegmentKeyOk() (*string, bool)`

GetSegmentKeyOk returns a tuple with the SegmentKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKey

`func (o *RolloutSegment) SetSegmentKey(v string)`

SetSegmentKey sets SegmentKey field to given value.

### HasSegmentKey

`func (o *RolloutSegment) HasSegmentKey() bool`

HasSegmentKey returns a boolean if a field has been set.

### GetValue

`func (o *RolloutSegment) GetValue() bool`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *RolloutSegment) GetValueOk() (*bool, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *RolloutSegment) SetValue(v bool)`

SetValue sets Value field to given value.

### HasValue

`func (o *RolloutSegment) HasValue() bool`

HasValue returns a boolean if a field has been set.

### GetSegmentKeys

`func (o *RolloutSegment) GetSegmentKeys() []string`

GetSegmentKeys returns the SegmentKeys field if non-nil, zero value otherwise.

### GetSegmentKeysOk

`func (o *RolloutSegment) GetSegmentKeysOk() (*[]string, bool)`

GetSegmentKeysOk returns a tuple with the SegmentKeys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKeys

`func (o *RolloutSegment) SetSegmentKeys(v []string)`

SetSegmentKeys sets SegmentKeys field to given value.

### HasSegmentKeys

`func (o *RolloutSegment) HasSegmentKeys() bool`

HasSegmentKeys returns a boolean if a field has been set.

### GetSegmentOperator

`func (o *RolloutSegment) GetSegmentOperator() string`

GetSegmentOperator returns the SegmentOperator field if non-nil, zero value otherwise.

### GetSegmentOperatorOk

`func (o *RolloutSegment) GetSegmentOperatorOk() (*string, bool)`

GetSegmentOperatorOk returns a tuple with the SegmentOperator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentOperator

`func (o *RolloutSegment) SetSegmentOperator(v string)`

SetSegmentOperator sets SegmentOperator field to given value.

### HasSegmentOperator

`func (o *RolloutSegment) HasSegmentOperator() bool`

HasSegmentOperator returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


