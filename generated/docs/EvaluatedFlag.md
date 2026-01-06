# EvaluatedFlag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | Pointer to **string** |  | [optional] 
**Reason** | Pointer to **string** |  | [optional] 
**Variant** | Pointer to **string** |  | [optional] 
**Metadata** | Pointer to **map[string]interface{}** |  | [optional] 
**Value** | Pointer to **interface{}** | Represents a dynamically typed value which can be either null, a number, a string, a boolean, a recursive struct value, or a list of values. | [optional] 

## Methods

### NewEvaluatedFlag

`func NewEvaluatedFlag() *EvaluatedFlag`

NewEvaluatedFlag instantiates a new EvaluatedFlag object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEvaluatedFlagWithDefaults

`func NewEvaluatedFlagWithDefaults() *EvaluatedFlag`

NewEvaluatedFlagWithDefaults instantiates a new EvaluatedFlag object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKey

`func (o *EvaluatedFlag) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *EvaluatedFlag) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *EvaluatedFlag) SetKey(v string)`

SetKey sets Key field to given value.

### HasKey

`func (o *EvaluatedFlag) HasKey() bool`

HasKey returns a boolean if a field has been set.

### GetReason

`func (o *EvaluatedFlag) GetReason() string`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *EvaluatedFlag) GetReasonOk() (*string, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *EvaluatedFlag) SetReason(v string)`

SetReason sets Reason field to given value.

### HasReason

`func (o *EvaluatedFlag) HasReason() bool`

HasReason returns a boolean if a field has been set.

### GetVariant

`func (o *EvaluatedFlag) GetVariant() string`

GetVariant returns the Variant field if non-nil, zero value otherwise.

### GetVariantOk

`func (o *EvaluatedFlag) GetVariantOk() (*string, bool)`

GetVariantOk returns a tuple with the Variant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariant

`func (o *EvaluatedFlag) SetVariant(v string)`

SetVariant sets Variant field to given value.

### HasVariant

`func (o *EvaluatedFlag) HasVariant() bool`

HasVariant returns a boolean if a field has been set.

### GetMetadata

`func (o *EvaluatedFlag) GetMetadata() map[string]interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *EvaluatedFlag) GetMetadataOk() (*map[string]interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *EvaluatedFlag) SetMetadata(v map[string]interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *EvaluatedFlag) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetValue

`func (o *EvaluatedFlag) GetValue() interface{}`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *EvaluatedFlag) GetValueOk() (*interface{}, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *EvaluatedFlag) SetValue(v interface{})`

SetValue sets Value field to given value.

### HasValue

`func (o *EvaluatedFlag) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *EvaluatedFlag) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *EvaluatedFlag) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


