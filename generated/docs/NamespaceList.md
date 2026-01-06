# NamespaceList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Namespaces** | Pointer to [**[]Namespace**](Namespace.md) |  | [optional] 
**NextPageToken** | Pointer to **string** |  | [optional] 
**TotalCount** | Pointer to **int32** |  | [optional] 

## Methods

### NewNamespaceList

`func NewNamespaceList() *NamespaceList`

NewNamespaceList instantiates a new NamespaceList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNamespaceListWithDefaults

`func NewNamespaceListWithDefaults() *NamespaceList`

NewNamespaceListWithDefaults instantiates a new NamespaceList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetNamespaces

`func (o *NamespaceList) GetNamespaces() []Namespace`

GetNamespaces returns the Namespaces field if non-nil, zero value otherwise.

### GetNamespacesOk

`func (o *NamespaceList) GetNamespacesOk() (*[]Namespace, bool)`

GetNamespacesOk returns a tuple with the Namespaces field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNamespaces

`func (o *NamespaceList) SetNamespaces(v []Namespace)`

SetNamespaces sets Namespaces field to given value.

### HasNamespaces

`func (o *NamespaceList) HasNamespaces() bool`

HasNamespaces returns a boolean if a field has been set.

### GetNextPageToken

`func (o *NamespaceList) GetNextPageToken() string`

GetNextPageToken returns the NextPageToken field if non-nil, zero value otherwise.

### GetNextPageTokenOk

`func (o *NamespaceList) GetNextPageTokenOk() (*string, bool)`

GetNextPageTokenOk returns a tuple with the NextPageToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextPageToken

`func (o *NamespaceList) SetNextPageToken(v string)`

SetNextPageToken sets NextPageToken field to given value.

### HasNextPageToken

`func (o *NamespaceList) HasNextPageToken() bool`

HasNextPageToken returns a boolean if a field has been set.

### GetTotalCount

`func (o *NamespaceList) GetTotalCount() int32`

GetTotalCount returns the TotalCount field if non-nil, zero value otherwise.

### GetTotalCountOk

`func (o *NamespaceList) GetTotalCountOk() (*int32, bool)`

GetTotalCountOk returns a tuple with the TotalCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalCount

`func (o *NamespaceList) SetTotalCount(v int32)`

SetTotalCount sets TotalCount field to given value.

### HasTotalCount

`func (o *NamespaceList) HasTotalCount() bool`

HasTotalCount returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


