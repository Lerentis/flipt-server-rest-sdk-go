# \DistributionsServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateDistribution**](DistributionsServiceAPI.md#CreateDistribution) | **Post** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{ruleId}/distributions | 
[**DeleteDistribution**](DistributionsServiceAPI.md#DeleteDistribution) | **Delete** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{ruleId}/distributions/{id} | 
[**UpdateDistribution**](DistributionsServiceAPI.md#UpdateDistribution) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{ruleId}/distributions/{id} | 



## CreateDistribution

> Distribution CreateDistribution(ctx, namespaceKey, flagKey, ruleId).CreateDistributionRequest(createDistributionRequest).Execute()



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
	namespaceKey := "namespaceKey_example" // string | 
	flagKey := "flagKey_example" // string | 
	ruleId := "ruleId_example" // string | 
	createDistributionRequest := *openapiclient.NewCreateDistributionRequest("VariantId_example", float32(123)) // CreateDistributionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DistributionsServiceAPI.CreateDistribution(context.Background(), namespaceKey, flagKey, ruleId).CreateDistributionRequest(createDistributionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DistributionsServiceAPI.CreateDistribution``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateDistribution`: Distribution
	fmt.Fprintf(os.Stdout, "Response from `DistributionsServiceAPI.CreateDistribution`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**flagKey** | **string** |  | 
**ruleId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateDistributionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **createDistributionRequest** | [**CreateDistributionRequest**](CreateDistributionRequest.md) |  | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteDistribution

> DeleteDistribution(ctx, namespaceKey, flagKey, ruleId, id).VariantId(variantId).Execute()



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
	namespaceKey := "namespaceKey_example" // string | 
	flagKey := "flagKey_example" // string | 
	ruleId := "ruleId_example" // string | 
	id := "id_example" // string | 
	variantId := "variantId_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DistributionsServiceAPI.DeleteDistribution(context.Background(), namespaceKey, flagKey, ruleId, id).VariantId(variantId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DistributionsServiceAPI.DeleteDistribution``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**flagKey** | **string** |  | 
**ruleId** | **string** |  | 
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteDistributionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **variantId** | **string** |  | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateDistribution

> Distribution UpdateDistribution(ctx, namespaceKey, flagKey, ruleId, id).UpdateDistributionRequest(updateDistributionRequest).Execute()



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
	namespaceKey := "namespaceKey_example" // string | 
	flagKey := "flagKey_example" // string | 
	ruleId := "ruleId_example" // string | 
	id := "id_example" // string | 
	updateDistributionRequest := *openapiclient.NewUpdateDistributionRequest("VariantId_example", float32(123)) // UpdateDistributionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DistributionsServiceAPI.UpdateDistribution(context.Background(), namespaceKey, flagKey, ruleId, id).UpdateDistributionRequest(updateDistributionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DistributionsServiceAPI.UpdateDistribution``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateDistribution`: Distribution
	fmt.Fprintf(os.Stdout, "Response from `DistributionsServiceAPI.UpdateDistribution`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**flagKey** | **string** |  | 
**ruleId** | **string** |  | 
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateDistributionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **updateDistributionRequest** | [**UpdateDistributionRequest**](UpdateDistributionRequest.md) |  | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

