# GetProviderConfigurationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** |  | [optional] 
**Capabilities** | Pointer to [**Capabilities**](Capabilities.md) |  | [optional] 

## Methods

### NewGetProviderConfigurationResponse

`func NewGetProviderConfigurationResponse() *GetProviderConfigurationResponse`

NewGetProviderConfigurationResponse instantiates a new GetProviderConfigurationResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetProviderConfigurationResponseWithDefaults

`func NewGetProviderConfigurationResponseWithDefaults() *GetProviderConfigurationResponse`

NewGetProviderConfigurationResponseWithDefaults instantiates a new GetProviderConfigurationResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *GetProviderConfigurationResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GetProviderConfigurationResponse) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GetProviderConfigurationResponse) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *GetProviderConfigurationResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### GetCapabilities

`func (o *GetProviderConfigurationResponse) GetCapabilities() Capabilities`

GetCapabilities returns the Capabilities field if non-nil, zero value otherwise.

### GetCapabilitiesOk

`func (o *GetProviderConfigurationResponse) GetCapabilitiesOk() (*Capabilities, bool)`

GetCapabilitiesOk returns a tuple with the Capabilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCapabilities

`func (o *GetProviderConfigurationResponse) SetCapabilities(v Capabilities)`

SetCapabilities sets Capabilities field to given value.

### HasCapabilities

`func (o *GetProviderConfigurationResponse) HasCapabilities() bool`

HasCapabilities returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


