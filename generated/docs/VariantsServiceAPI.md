# \VariantsServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateVariant**](VariantsServiceAPI.md#CreateVariant) | **Post** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/variants | 
[**DeleteVariant**](VariantsServiceAPI.md#DeleteVariant) | **Delete** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/variants/{id} | 
[**UpdateVariant**](VariantsServiceAPI.md#UpdateVariant) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/variants/{id} | 



## CreateVariant

> Variant CreateVariant(ctx, namespaceKey, flagKey).CreateVariantRequest(createVariantRequest).Execute()



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
	namespaceKey := "namespaceKey_example" // string | 
	flagKey := "flagKey_example" // string | 
	createVariantRequest := *openapiclient.NewCreateVariantRequest("Key_example") // CreateVariantRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.VariantsServiceAPI.CreateVariant(context.Background(), namespaceKey, flagKey).CreateVariantRequest(createVariantRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VariantsServiceAPI.CreateVariant``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateVariant`: Variant
	fmt.Fprintf(os.Stdout, "Response from `VariantsServiceAPI.CreateVariant`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**flagKey** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateVariantRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **createVariantRequest** | [**CreateVariantRequest**](CreateVariantRequest.md) |  | 

### Return type

[**Variant**](Variant.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteVariant

> DeleteVariant(ctx, namespaceKey, flagKey, id).Execute()



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
	namespaceKey := "namespaceKey_example" // string | 
	flagKey := "flagKey_example" // string | 
	id := "id_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.VariantsServiceAPI.DeleteVariant(context.Background(), namespaceKey, flagKey, id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VariantsServiceAPI.DeleteVariant``: %v\n", err)
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
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteVariantRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




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


## UpdateVariant

> Variant UpdateVariant(ctx, namespaceKey, flagKey, id).UpdateVariantRequest(updateVariantRequest).Execute()



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
	namespaceKey := "namespaceKey_example" // string | 
	flagKey := "flagKey_example" // string | 
	id := "id_example" // string | 
	updateVariantRequest := *openapiclient.NewUpdateVariantRequest("Key_example") // UpdateVariantRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.VariantsServiceAPI.UpdateVariant(context.Background(), namespaceKey, flagKey, id).UpdateVariantRequest(updateVariantRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VariantsServiceAPI.UpdateVariant``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateVariant`: Variant
	fmt.Fprintf(os.Stdout, "Response from `VariantsServiceAPI.UpdateVariant`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**flagKey** | **string** |  | 
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateVariantRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **updateVariantRequest** | [**UpdateVariantRequest**](UpdateVariantRequest.md) |  | 

### Return type

[**Variant**](Variant.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

