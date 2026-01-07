# \AuthenticationMethodKubernetesServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**KubernetesVerifyServiceAccount**](AuthenticationMethodKubernetesServiceAPI.md#KubernetesVerifyServiceAccount) | **Post** /auth/v1/method/kubernetes/serviceaccount | 



## KubernetesVerifyServiceAccount

> VerifyServiceAccountResponse KubernetesVerifyServiceAccount(ctx).VerifyServiceAccountRequest(verifyServiceAccountRequest).Execute()



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
	verifyServiceAccountRequest := *openapiclient.NewVerifyServiceAccountRequest() // VerifyServiceAccountRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationMethodKubernetesServiceAPI.KubernetesVerifyServiceAccount(context.Background()).VerifyServiceAccountRequest(verifyServiceAccountRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationMethodKubernetesServiceAPI.KubernetesVerifyServiceAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `KubernetesVerifyServiceAccount`: VerifyServiceAccountResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationMethodKubernetesServiceAPI.KubernetesVerifyServiceAccount`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiKubernetesVerifyServiceAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verifyServiceAccountRequest** | [**VerifyServiceAccountRequest**](VerifyServiceAccountRequest.md) |  | 

### Return type

[**VerifyServiceAccountResponse**](VerifyServiceAccountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

