# CreateSegmentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | **string** |  | 
**Name** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**MatchType** | **string** |  | 
**NamespaceKey** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateSegmentRequest

`func NewCreateSegmentRequest(key string, name string, matchType string, ) *CreateSegmentRequest`

NewCreateSegmentRequest instantiates a new CreateSegmentRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateSegmentRequestWithDefaults

`func NewCreateSegmentRequestWithDefaults() *CreateSegmentRequest`

NewCreateSegmentRequestWithDefaults instantiates a new CreateSegmentRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKey

`func (o *CreateSegmentRequest) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *CreateSegmentRequest) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *CreateSegmentRequest) SetKey(v string)`

SetKey sets Key field to given value.


### GetName

`func (o *CreateSegmentRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateSegmentRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateSegmentRequest) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CreateSegmentRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateSegmentRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateSegmentRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateSegmentRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetMatchType

`func (o *CreateSegmentRequest) GetMatchType() string`

GetMatchType returns the MatchType field if non-nil, zero value otherwise.

### GetMatchTypeOk

`func (o *CreateSegmentRequest) GetMatchTypeOk() (*string, bool)`

GetMatchTypeOk returns a tuple with the MatchType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchType

`func (o *CreateSegmentRequest) SetMatchType(v string)`

SetMatchType sets MatchType field to given value.


### GetNamespaceKey

`func (o *CreateSegmentRequest) GetNamespaceKey() string`

GetNamespaceKey returns the NamespaceKey field if non-nil, zero value otherwise.

### GetNamespaceKeyOk

`func (o *CreateSegmentRequest) GetNamespaceKeyOk() (*string, bool)`

GetNamespaceKeyOk returns a tuple with the NamespaceKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaceKey

`func (o *CreateSegmentRequest) SetNamespaceKey(v string)`

SetNamespaceKey sets NamespaceKey field to given value.

### HasNamespaceKey

`func (o *CreateSegmentRequest) HasNamespaceKey() bool`

HasNamespaceKey returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


