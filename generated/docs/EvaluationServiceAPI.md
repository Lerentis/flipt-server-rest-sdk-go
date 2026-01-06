# \EvaluationServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**EvaluateBatch**](EvaluationServiceAPI.md#EvaluateBatch) | **Post** /evaluate/v1/batch | 
[**EvaluateBoolean**](EvaluationServiceAPI.md#EvaluateBoolean) | **Post** /evaluate/v1/boolean | 
[**EvaluateVariant**](EvaluationServiceAPI.md#EvaluateVariant) | **Post** /evaluate/v1/variant | 



## EvaluateBatch

> BatchEvaluationResponse EvaluateBatch(ctx).BatchEvaluationRequest(batchEvaluationRequest).Execute()



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
	batchEvaluationRequest := *openapiclient.NewBatchEvaluationRequest([]openapiclient.EvaluationRequest{*openapiclient.NewEvaluationRequest("NamespaceKey_example", "FlagKey_example", "EntityId_example", map[string]string{"key": "Inner_example"})}) // BatchEvaluationRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EvaluationServiceAPI.EvaluateBatch(context.Background()).BatchEvaluationRequest(batchEvaluationRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EvaluationServiceAPI.EvaluateBatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EvaluateBatch`: BatchEvaluationResponse
	fmt.Fprintf(os.Stdout, "Response from `EvaluationServiceAPI.EvaluateBatch`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiEvaluateBatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batchEvaluationRequest** | [**BatchEvaluationRequest**](BatchEvaluationRequest.md) |  | 

### Return type

[**BatchEvaluationResponse**](BatchEvaluationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## EvaluateBoolean

> BooleanEvaluationResponse EvaluateBoolean(ctx).EvaluationRequest(evaluationRequest).Execute()



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
	evaluationRequest := *openapiclient.NewEvaluationRequest("NamespaceKey_example", "FlagKey_example", "EntityId_example", map[string]string{"key": "Inner_example"}) // EvaluationRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EvaluationServiceAPI.EvaluateBoolean(context.Background()).EvaluationRequest(evaluationRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EvaluationServiceAPI.EvaluateBoolean``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EvaluateBoolean`: BooleanEvaluationResponse
	fmt.Fprintf(os.Stdout, "Response from `EvaluationServiceAPI.EvaluateBoolean`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiEvaluateBooleanRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluationRequest** | [**EvaluationRequest**](EvaluationRequest.md) |  | 

### Return type

[**BooleanEvaluationResponse**](BooleanEvaluationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## EvaluateVariant

> VariantEvaluationResponse EvaluateVariant(ctx).EvaluationRequest(evaluationRequest).Execute()



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
	evaluationRequest := *openapiclient.NewEvaluationRequest("NamespaceKey_example", "FlagKey_example", "EntityId_example", map[string]string{"key": "Inner_example"}) // EvaluationRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EvaluationServiceAPI.EvaluateVariant(context.Background()).EvaluationRequest(evaluationRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EvaluationServiceAPI.EvaluateVariant``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `EvaluateVariant`: VariantEvaluationResponse
	fmt.Fprintf(os.Stdout, "Response from `EvaluationServiceAPI.EvaluateVariant`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiEvaluateVariantRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluationRequest** | [**EvaluationRequest**](EvaluationRequest.md) |  | 

### Return type

[**VariantEvaluationResponse**](VariantEvaluationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

