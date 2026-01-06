# \AuthenticationMethodTokenServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateMethodToken**](AuthenticationMethodTokenServiceAPI.md#CreateMethodToken) | **Post** /auth/v1/method/token | 



## CreateMethodToken

> CreateTokenResponse CreateMethodToken(ctx).CreateTokenRequest(createTokenRequest).Execute()



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/lerentis/flipt-server-rest-sdk-go"
)

func main() {
	createTokenRequest := *openapiclient.NewCreateTokenRequest() // CreateTokenRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationMethodTokenServiceAPI.CreateMethodToken(context.Background()).CreateTokenRequest(createTokenRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationMethodTokenServiceAPI.CreateMethodToken``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateMethodToken`: CreateTokenResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationMethodTokenServiceAPI.CreateMethodToken`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateMethodTokenRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createTokenRequest** | [**CreateTokenRequest**](CreateTokenRequest.md) |  | 

### Return type

[**CreateTokenResponse**](CreateTokenResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

