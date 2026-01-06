# ListAuthenticationsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Authentications** | Pointer to [**[]Authentication**](Authentication.md) |  | [optional] 
**NextPageToken** | Pointer to **string** |  | [optional] 

## Methods

### NewListAuthenticationsResponse

`func NewListAuthenticationsResponse() *ListAuthenticationsResponse`

NewListAuthenticationsResponse instantiates a new ListAuthenticationsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListAuthenticationsResponseWithDefaults

`func NewListAuthenticationsResponseWithDefaults() *ListAuthenticationsResponse`

NewListAuthenticationsResponseWithDefaults instantiates a new ListAuthenticationsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthentications

`func (o *ListAuthenticationsResponse) GetAuthentications() []Authentication`

GetAuthentications returns the Authentications field if non-nil, zero value otherwise.

### GetAuthenticationsOk

`func (o *ListAuthenticationsResponse) GetAuthenticationsOk() (*[]Authentication, bool)`

GetAuthenticationsOk returns a tuple with the Authentications field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthentications

`func (o *ListAuthenticationsResponse) SetAuthentications(v []Authentication)`

SetAuthentications sets Authentications field to given value.

### HasAuthentications

`func (o *ListAuthenticationsResponse) HasAuthentications() bool`

HasAuthentications returns a boolean if a field has been set.

### GetNextPageToken

`func (o *ListAuthenticationsResponse) GetNextPageToken() string`

GetNextPageToken returns the NextPageToken field if non-nil, zero value otherwise.

### GetNextPageTokenOk

`func (o *ListAuthenticationsResponse) GetNextPageTokenOk() (*string, bool)`

GetNextPageTokenOk returns a tuple with the NextPageToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextPageToken

`func (o *ListAuthenticationsResponse) SetNextPageToken(v string)`

SetNextPageToken sets NextPageToken field to given value.

### HasNextPageToken

`func (o *ListAuthenticationsResponse) HasNextPageToken() bool`

HasNextPageToken returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


