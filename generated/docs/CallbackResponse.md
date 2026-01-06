# CallbackResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClientToken** | Pointer to **string** |  | [optional] 
**Authentication** | Pointer to [**Authentication**](Authentication.md) |  | [optional] 

## Methods

### NewCallbackResponse

`func NewCallbackResponse() *CallbackResponse`

NewCallbackResponse instantiates a new CallbackResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCallbackResponseWithDefaults

`func NewCallbackResponseWithDefaults() *CallbackResponse`

NewCallbackResponseWithDefaults instantiates a new CallbackResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClientToken

`func (o *CallbackResponse) GetClientToken() string`

GetClientToken returns the ClientToken field if non-nil, zero value otherwise.

### GetClientTokenOk

`func (o *CallbackResponse) GetClientTokenOk() (*string, bool)`

GetClientTokenOk returns a tuple with the ClientToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientToken

`func (o *CallbackResponse) SetClientToken(v string)`

SetClientToken sets ClientToken field to given value.

### HasClientToken

`func (o *CallbackResponse) HasClientToken() bool`

HasClientToken returns a boolean if a field has been set.

### GetAuthentication

`func (o *CallbackResponse) GetAuthentication() Authentication`

GetAuthentication returns the Authentication field if non-nil, zero value otherwise.

### GetAuthenticationOk

`func (o *CallbackResponse) GetAuthenticationOk() (*Authentication, bool)`

GetAuthenticationOk returns a tuple with the Authentication field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthentication

`func (o *CallbackResponse) SetAuthentication(v Authentication)`

SetAuthentication sets Authentication field to given value.

### HasAuthentication

`func (o *CallbackResponse) HasAuthentication() bool`

HasAuthentication returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


