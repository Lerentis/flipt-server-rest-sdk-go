# UpdateFlagRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | Pointer to **string** |  | [optional] 
**Name** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Enabled** | Pointer to **bool** |  | [optional] 
**NamespaceKey** | Pointer to **string** |  | [optional] 
**DefaultVariantId** | Pointer to **string** |  | [optional] 
**Metadata** | Pointer to **map[string]interface{}** |  | [optional] 

## Methods

### NewUpdateFlagRequest

`func NewUpdateFlagRequest(name string, ) *UpdateFlagRequest`

NewUpdateFlagRequest instantiates a new UpdateFlagRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateFlagRequestWithDefaults

`func NewUpdateFlagRequestWithDefaults() *UpdateFlagRequest`

NewUpdateFlagRequestWithDefaults instantiates a new UpdateFlagRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKey

`func (o *UpdateFlagRequest) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *UpdateFlagRequest) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *UpdateFlagRequest) SetKey(v string)`

SetKey sets Key field to given value.

### HasKey

`func (o *UpdateFlagRequest) HasKey() bool`

HasKey returns a boolean if a field has been set.

### GetName

`func (o *UpdateFlagRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateFlagRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpdateFlagRequest) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *UpdateFlagRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *UpdateFlagRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *UpdateFlagRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *UpdateFlagRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEnabled

`func (o *UpdateFlagRequest) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *UpdateFlagRequest) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *UpdateFlagRequest) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *UpdateFlagRequest) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetNamespaceKey

`func (o *UpdateFlagRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *UpdateFlagRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *UpdateFlagRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *UpdateFlagRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.

### GetDefaultVariantId

`func (o *UpdateFlagRequest) GetDefaultVariantId() string`

GetDefaultVariantId returns the DefaultVariantId field if non-nil, zero value otherwise.

### GetDefaultVariantIdOk

`func (o *UpdateFlagRequest) GetDefaultVariantIdOk() (*string, bool)`

GetDefaultVariantIdOk returns a tuple with the DefaultVariantId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultVariantId

`func (o *UpdateFlagRequest) SetDefaultVariantId(v string)`

SetDefaultVariantId sets DefaultVariantId field to given value.

### HasDefaultVariantId

`func (o *UpdateFlagRequest) HasDefaultVariantId() bool`

HasDefaultVariantId returns a boolean if a field has been set.

### GetMetadata

`func (o *UpdateFlagRequest) GetMetadata() map[string]interface{}`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *UpdateFlagRequest) GetMetadataOk() (*map[string]interface{}, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *UpdateFlagRequest) SetMetadata(v map[string]interface{})`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *UpdateFlagRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


