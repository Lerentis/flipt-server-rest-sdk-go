# \AuthenticationMethodOIDCServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**OidcAuthorizeURL**](AuthenticationMethodOIDCServiceAPI.md#OidcAuthorizeURL) | **Get** /auth/v1/method/oidc/{provider}/authorize | 
[**OidcCallback**](AuthenticationMethodOIDCServiceAPI.md#OidcCallback) | **Get** /auth/v1/method/oidc/{provider}/callback | 



## OidcAuthorizeURL

> AuthorizeURLResponse OidcAuthorizeURL(ctx, provider).State(state).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/lerentis/flipt-server-rest-sdk-go/generated"
)

func main() {
	provider := "provider_example" // string | 
	state := "state_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationMethodOIDCServiceAPI.OidcAuthorizeURL(context.Background(), provider).State(state).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationMethodOIDCServiceAPI.OidcAuthorizeURL``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `OidcAuthorizeURL`: AuthorizeURLResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationMethodOIDCServiceAPI.OidcAuthorizeURL`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiOidcAuthorizeURLRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **state** | **string** |  | 

### Return type

[**AuthorizeURLResponse**](AuthorizeURLResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## OidcCallback

> CallbackResponse OidcCallback(ctx, provider).Code(code).State(state).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/lerentis/flipt-server-rest-sdk-go/generated"
)

func main() {
	provider := "provider_example" // string | 
	code := "code_example" // string |  (optional)
	state := "state_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationMethodOIDCServiceAPI.OidcCallback(context.Background(), provider).Code(code).State(state).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationMethodOIDCServiceAPI.OidcCallback``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `OidcCallback`: CallbackResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationMethodOIDCServiceAPI.OidcCallback`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**provider** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiOidcCallbackRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **code** | **string** |  | 
 **state** | **string** |  | 

### Return type

[**CallbackResponse**](CallbackResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

