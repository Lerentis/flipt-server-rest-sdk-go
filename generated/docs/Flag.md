# Flag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | Pointer to **string** |  | [optional] 
**Name** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 
**Variants** | Pointer to [**[]Variant**](Variant.md) |  | [optional] 
**NamespaceKey** | Pointer to **string** |  | [optional] 
**Type** | Pointer to **string** |  | [optional] 
**DefaultVariant** | Pointer to [**Variant**](Variant.md) |  | [optional] 
**Metadata** | Pointer to **map[string]interface{}** |  | [optional] 

## Methods

### NewFlag

`func NewFlag() *Flag`

NewFlag instantiates a new Flag object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFlagWithDefaults

`func NewFlagWithDefaults() *Flag`

NewFlagWithDefaults instantiates a new Flag object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKey

`func (o *Flag) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *Flag) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *Flag) SetKey(v string)`

SetKey sets Key field to given value.

### HasKey

`func (o *Flag) HasKey() bool`

HasKey returns a boolean if a field has been set.

### GetName

`func (o *Flag) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Flag) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Flag) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Flag) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *Flag) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Flag) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Flag) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Flag) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEnabled

`func (o *Flag) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *Flag) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *Flag) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *Flag) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Flag) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Flag) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Flag) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Flag) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *Flag) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Flag) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Flag) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *Flag) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetVariants

`func (o *Flag) GetVariants() []Variant`

GetVariants returns the Variants field if non-nil, zero value otherwise.

### GetVariantsOk

`func (o *Flag) GetVariantsOk() (*[]Variant, bool)`

GetVariantsOk returns a tuple with the Variants field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariants

`func (o *Flag) SetVariants(v []Variant)`

SetVariants sets Variants field to given value.

### HasVariants

`func (o *Flag) HasVariants() bool`

HasVariants returns a boolean if a field has been set.

### GetNamespaceKey

`func (o *Flag) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *Flag) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *Flag) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *Flag) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetType

`func (o *Flag) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Flag) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Flag) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *Flag) HasType() bool`

HasType returns a boolean if a field has been set.

### GetDefaultVariant

`func (o *Flag) GetDefaultVariant() Variant`

GetDefaultVariant returns the DefaultVariant field if non-nil, zero value otherwise.

### GetDefaultVariantOk

`func (o *Flag) GetDefaultVariantOk() (*Variant, bool)`

GetDefaultVariantOk returns a tuple with the DefaultVariant field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultVariant

`func (o *Flag) SetDefaultVariant(v Variant)`

SetDefaultVariant sets DefaultVariant field to given value.

### HasDefaultVariant

`func (o *Flag) HasDefaultVariant() bool`

HasDefaultVariant returns a boolean if a field has been set.

### GetMetadata

`func (o *Flag) GetMetadata() map[string]interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *Flag) GetMetadataOk() (*map[string]interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *Flag) SetMetadata(v map[string]interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *Flag) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


