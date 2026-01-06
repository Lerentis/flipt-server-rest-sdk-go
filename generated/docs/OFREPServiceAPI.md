# \OFREPServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**OfrepConfiguration**](OFREPServiceAPI.md#OfrepConfiguration) | **Get** /ofrep/v1/configuration | 
[**OfrepEvaluateBulk**](OFREPServiceAPI.md#OfrepEvaluateBulk) | **Post** /ofrep/v1/evaluate/flags | 
[**OfrepEvaluateFlag**](OFREPServiceAPI.md#OfrepEvaluateFlag) | **Post** /ofrep/v1/evaluate/flags/{key} | 



## OfrepConfiguration

> GetProviderConfigurationResponse OfrepConfiguration(ctx).Execute()





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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OFREPServiceAPI.OfrepConfiguration(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OFREPServiceAPI.OfrepConfiguration``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `OfrepConfiguration`: GetProviderConfigurationResponse
	fmt.Fprintf(os.Stdout, "Response from `OFREPServiceAPI.OfrepConfiguration`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiOfrepConfigurationRequest struct via the builder pattern


### Return type

[**GetProviderConfigurationResponse**](GetProviderConfigurationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## OfrepEvaluateBulk

> BulkEvaluationResponse OfrepEvaluateBulk(ctx).EvaluateBulkRequest(evaluateBulkRequest).Execute()





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
	evaluateBulkRequest := *openapiclient.NewEvaluateBulkRequest() // EvaluateBulkRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OFREPServiceAPI.OfrepEvaluateBulk(context.Background()).EvaluateBulkRequest(evaluateBulkRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OFREPServiceAPI.OfrepEvaluateBulk``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `OfrepEvaluateBulk`: BulkEvaluationResponse
	fmt.Fprintf(os.Stdout, "Response from `OFREPServiceAPI.OfrepEvaluateBulk`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiOfrepEvaluateBulkRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluateBulkRequest** | [**EvaluateBulkRequest**](EvaluateBulkRequest.md) |  | 

### Return type

[**BulkEvaluationResponse**](BulkEvaluationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## OfrepEvaluateFlag

> EvaluatedFlag OfrepEvaluateFlag(ctx, key).EvaluateFlagRequest(evaluateFlagRequest).Execute()





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
	key := "key_example" // string | 
	evaluateFlagRequest := *openapiclient.NewEvaluateFlagRequest() // EvaluateFlagRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.OFREPServiceAPI.OfrepEvaluateFlag(context.Background(), key).EvaluateFlagRequest(evaluateFlagRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `OFREPServiceAPI.OfrepEvaluateFlag``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `OfrepEvaluateFlag`: EvaluatedFlag
	fmt.Fprintf(os.Stdout, "Response from `OFREPServiceAPI.OfrepEvaluateFlag`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**key** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiOfrepEvaluateFlagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **evaluateFlagRequest** | [**EvaluateFlagRequest**](EvaluateFlagRequest.md) |  | 

### Return type

[**EvaluatedFlag**](EvaluatedFlag.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

