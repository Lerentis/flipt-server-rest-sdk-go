# EvaluationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | Pointer to **string** |  | [optional] 
**BooleanResponse** | Pointer to [**BooleanEvaluationResponse**](BooleanEvaluationResponse.md) |  | [optional] 
**VariantResponse** | Pointer to [**VariantEvaluationResponse**](VariantEvaluationResponse.md) |  | [optional] 
**ErrorResponse** | Pointer to [**ErrorEvaluationResponse**](ErrorEvaluationResponse.md) |  | [optional] 

## Methods

### NewEvaluationResponse

`func NewEvaluationResponse() *EvaluationResponse`

NewEvaluationResponse instantiates a new EvaluationResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEvaluationResponseWithDefaults

`func NewEvaluationResponseWithDefaults() *EvaluationResponse`

NewEvaluationResponseWithDefaults instantiates a new EvaluationResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *EvaluationResponse) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *EvaluationResponse) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *EvaluationResponse) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *EvaluationResponse) HasType() bool`

HasType returns a boolean if a field has been set.

### GetBooleanResponse

`func (o *EvaluationResponse) GetBooleanResponse() BooleanEvaluationResponse`

GetBooleanResponse returns the BooleanResponse field if non-nil, zero value otherwise.

### GetBooleanResponseOk

`func (o *EvaluationResponse) GetBooleanResponseOk() (*BooleanEvaluationResponse, bool)`

GetBooleanResponseOk returns a tuple with the BooleanResponse field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBooleanResponse

`func (o *EvaluationResponse) SetBooleanResponse(v BooleanEvaluationResponse)`

SetBooleanResponse sets BooleanResponse field to given value.

### HasBooleanResponse

`func (o *EvaluationResponse) HasBooleanResponse() bool`

HasBooleanResponse returns a boolean if a field has been set.

### GetVariantResponse

`func (o *EvaluationResponse) GetVariantResponse() VariantEvaluationResponse`

GetVariantResponse returns the VariantResponse field if non-nil, zero value otherwise.

### GetVariantResponseOk

`func (o *EvaluationResponse) GetVariantResponseOk() (*VariantEvaluationResponse, bool)`

GetVariantResponseOk returns a tuple with the VariantResponse field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVariantResponse

`func (o *EvaluationResponse) SetVariantResponse(v VariantEvaluationResponse)`

SetVariantResponse sets VariantResponse field to given value.

### HasVariantResponse

`func (o *EvaluationResponse) HasVariantResponse() bool`

HasVariantResponse returns a boolean if a field has been set.

### GetErrorResponse

`func (o *EvaluationResponse) GetErrorResponse() ErrorEvaluationResponse`

GetErrorResponse returns the ErrorResponse field if non-nil, zero value otherwise.

### GetErrorResponseOk

`func (o *EvaluationResponse) GetErrorResponseOk() (*ErrorEvaluationResponse, bool)`

GetErrorResponseOk returns a tuple with the ErrorResponse field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorResponse

`func (o *EvaluationResponse) SetErrorResponse(v ErrorEvaluationResponse)`

SetErrorResponse sets ErrorResponse field to given value.

### HasErrorResponse

`func (o *EvaluationResponse) HasErrorResponse() bool`

HasErrorResponse returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


