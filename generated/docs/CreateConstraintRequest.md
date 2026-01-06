# CreateConstraintRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SegmentKey** | Pointer to **string** |  | [optional] 
**Type** | **string** |  | 
**Property** | **string** |  | 
**Operator** | **string** |  | 
**Value** | Pointer to **string** |  | [optional] 
**NamespaceKey** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateConstraintRequest

`func NewCreateConstraintRequest(type_ string, property string, operator string, ) *CreateConstraintRequest`

NewCreateConstraintRequest instantiates a new CreateConstraintRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateConstraintRequestWithDefaults

`func NewCreateConstraintRequestWithDefaults() *CreateConstraintRequest`

NewCreateConstraintRequestWithDefaults instantiates a new CreateConstraintRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSegmentKey

`func (o *CreateConstraintRequest) GetSegmentKey() string`

GetSegmentKey returns the SegmentKey field if non-nil, zero value otherwise.

### GetSegmentKeyOk

`func (o *CreateConstraintRequest) GetSegmentKeyOk() (*string, bool)`

GetSegmentKeyOk returns a tuple with the SegmentKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKey

`func (o *CreateConstraintRequest) SetSegmentKey(v string)`

SetSegmentKey sets SegmentKey field to given value.

### HasSegmentKey

`func (o *CreateConstraintRequest) HasSegmentKey() bool`

HasSegmentKey returns a boolean if a field has been set.

### GetType

`func (o *CreateConstraintRequest) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *CreateConstraintRequest) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *CreateConstraintRequest) SetType(v string)`

SetType sets Type field to given value.


### GetProperty

`func (o *CreateConstraintRequest) GetProperty() string`

GetProperty returns the Property field if non-nil, zero value otherwise.

### GetPropertyOk

`func (o *CreateConstraintRequest) GetPropertyOk() (*string, bool)`

GetPropertyOk returns a tuple with the Property field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperty

`func (o *CreateConstraintRequest) SetProperty(v string)`

SetProperty sets Property field to given value.


### GetOperator

`func (o *CreateConstraintRequest) GetOperator() string`

GetOperator returns the Operator field if non-nil, zero value otherwise.

### GetOperatorOk

`func (o *CreateConstraintRequest) GetOperatorOk() (*string, bool)`

GetOperatorOk returns a tuple with the Operator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperator

`func (o *CreateConstraintRequest) SetOperator(v string)`

SetOperator sets Operator field to given value.


### GetValue

`func (o *CreateConstraintRequest) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *CreateConstraintRequest) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *CreateConstraintRequest) SetValue(v string)`

SetValue sets Value field to given value.

### HasValue

`func (o *CreateConstraintRequest) HasValue() bool`

HasValue returns a boolean if a field has been set.

### GetNamespaceKey

`func (o *CreateConstraintRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *CreateConstraintRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *CreateConstraintRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *CreateConstraintRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetDescription

`func (o *CreateConstraintRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateConstraintRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateConstraintRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateConstraintRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


