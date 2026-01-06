# Constraint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**SegmentKey** | Pointer to **string** |  | [optional] 
**Type** | Pointer to **string** |  | [optional] 
**Property** | Pointer to **string** |  | [optional] 
**Operator** | Pointer to **string** |  | [optional] 
**Value** | Pointer to **string** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**NamespaceKey** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 

## Methods

### NewConstraint

`func NewConstraint() *Constraint`

NewConstraint instantiates a new Constraint object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewConstraintWithDefaults

`func NewConstraintWithDefaults() *Constraint`

NewConstraintWithDefaults instantiates a new Constraint object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Constraint) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Constraint) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Constraint) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *Constraint) HasId() bool`

HasId returns a boolean if a field has been set.

### GetSegmentKey

`func (o *Constraint) GetSegmentKey() string`

GetSegmentKey returns the SegmentKey field if non-nil, zero value otherwise.

### GetSegmentKeyOk

`func (o *Constraint) GetSegmentKeyOk() (*string, bool)`

GetSegmentKeyOk returns a tuple with the SegmentKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSegmentKey

`func (o *Constraint) SetSegmentKey(v string)`

SetSegmentKey sets SegmentKey field to given value.

### HasSegmentKey

`func (o *Constraint) HasSegmentKey() bool`

HasSegmentKey returns a boolean if a field has been set.

### GetType

`func (o *Constraint) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Constraint) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Constraint) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *Constraint) HasType() bool`

HasType returns a boolean if a field has been set.

### GetProperty

`func (o *Constraint) GetProperty() string`

GetProperty returns the Property field if non-nil, zero value otherwise.

### GetPropertyOk

`func (o *Constraint) GetPropertyOk() (*string, bool)`

GetPropertyOk returns a tuple with the Property field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperty

`func (o *Constraint) SetProperty(v string)`

SetProperty sets Property field to given value.

### HasProperty

`func (o *Constraint) HasProperty() bool`

HasProperty returns a boolean if a field has been set.

### GetOperator

`func (o *Constraint) GetOperator() string`

GetOperator returns the Operator field if non-nil, zero value otherwise.

### GetOperatorOk

`func (o *Constraint) GetOperatorOk() (*string, bool)`

GetOperatorOk returns a tuple with the Operator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperator

`func (o *Constraint) SetOperator(v string)`

SetOperator sets Operator field to given value.

### HasOperator

`func (o *Constraint) HasOperator() bool`

HasOperator returns a boolean if a field has been set.

### GetValue

`func (o *Constraint) GetValue() string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *Constraint) GetValueOk() (*string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *Constraint) SetValue(v string)`

SetValue sets Value field to given value.

### HasValue

`func (o *Constraint) HasValue() bool`

HasValue returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Constraint) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Constraint) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Constraint) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Constraint) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *Constraint) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Constraint) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Constraint) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *Constraint) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetNamespaceKey

`func (o *Constraint) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *Constraint) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *Constraint) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *Constraint) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetDescription

`func (o *Constraint) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Constraint) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Constraint) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Constraint) HasDescription() bool`

HasDescription returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


