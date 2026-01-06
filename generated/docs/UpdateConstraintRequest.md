# UpdateConstraintRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**SegmentKey** | Pointer to **string** |  | [optional] 
**Type** | **string** |  | 
**Property** | **string** |  | 
**Operator** | **string** |  | 
**Value** | Pointer to **string** |  | [optional] 
**NamespaceKey** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 

## Methods

### NewUpdateConstraintRequest

`func NewUpdateConstraintRequest(type_ string, property string, operator string, ) *UpdateConstraintRequest`

NewUpdateConstraintRequest instantiates a new UpdateConstraintRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateConstraintRequestWithDefaults

`func NewUpdateConstraintRequestWithDefaults() *UpdateConstraintRequest`

NewUpdateConstraintRequestWithDefaults instantiates a new UpdateConstraintRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpdateConstraintRequest) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateConstraintRequest) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateConstraintRequest) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *UpdateConstraintRequest) HasId() bool`

HasId returns a boolean if a field has been set.

### GetSegmentKey

`func (o *UpdateConstraintRequest) GetSegmentKey() string`

GetSegmentKey returns the SegmentKey field if non-nil, zero value otherwise.

### GetSegmentKeyOk

`func (o *UpdateConstraintRequest) GetSegmentKeyOk() (*string, bool)`

GetSegmentKeyOk returns a tuple with the SegmentKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKey

`func (o *UpdateConstraintRequest) SetSegmentKey(v string)`

SetSegmentKey sets SegmentKey field to given value.

### HasSegmentKey

`func (o *UpdateConstraintRequest) HasSegmentKey() bool`

HasSegmentKey returns a boolean if a field has been set.

### GetType

`func (o *UpdateConstraintRequest) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *UpdateConstraintRequest) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *UpdateConstraintRequest) SetType(v string)`

SetType sets Type field to given value.


### GetProperty

`func (o *UpdateConstraintRequest) GetProperty() string`

GetProperty returns the Property field if non-nil, zero value otherwise.

### GetPropertyOk

`func (o *UpdateConstraintRequest) GetPropertyOk() (*string, bool)`

GetPropertyOk returns a tuple with the Property field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperty

`func (o *UpdateConstraintRequest) SetProperty(v string)`

SetProperty sets Property field to given value.


### GetOperator

`func (o *UpdateConstraintRequest) GetOperator() string`

GetOperator returns the Operator field if non-nil, zero value otherwise.

### GetOperatorOk

`func (o *UpdateConstraintRequest) GetOperatorOk() (*string, bool)`

GetOperatorOk returns a tuple with the Operator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperator

`func (o *UpdateConstraintRequest) SetOperator(v string)`

SetOperator sets Operator field to given value.


### GetValue

`func (o *UpdateConstraintRequest) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *UpdateConstraintRequest) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *UpdateConstraintRequest) SetValue(v string)`

SetValue sets Value field to given value.

### HasValue

`func (o *UpdateConstraintRequest) HasValue() bool`

HasValue returns a boolean if a field has been set.

### GetNamespaceKey

`func (o *UpdateConstraintRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *UpdateConstraintRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *UpdateConstraintRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *UpdateConstraintRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetDescription

`func (o *UpdateConstraintRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *UpdateConstraintRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *UpdateConstraintRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *UpdateConstraintRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


