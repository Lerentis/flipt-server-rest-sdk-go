# \RolloutsServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateRollout**](RolloutsServiceAPI.md#CreateRollout) | **Post** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts | 
[**DeleteRollout**](RolloutsServiceAPI.md#DeleteRollout) | **Delete** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts/{id} | 
[**GetRollout**](RolloutsServiceAPI.md#GetRollout) | **Get** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts/{id} | 
[**ListRollouts**](RolloutsServiceAPI.md#ListRollouts) | **Get** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts | 
[**OrderRollouts**](RolloutsServiceAPI.md#OrderRollouts) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts/order | 
[**UpdateRollout**](RolloutsServiceAPI.md#UpdateRollout) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts/{id} | 



## CreateRollout

> Rollout CreateRollout(ctx, namespaceKey, flagKey).CreateRolloutRequest(createRolloutRequest).Execute()



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
	createRolloutRequest := *openapiclient.NewCreateRolloutRequest(int32(123)) // CreateRolloutRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RolloutsServiceAPI.CreateRollout(context.Background(), namespaceKey, flagKey).CreateRolloutRequest(createRolloutRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolloutsServiceAPI.CreateRollout``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateRollout`: Rollout
	fmt.Fprintf(os.Stdout, "Response from `RolloutsServiceAPI.CreateRollout`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**flagKey** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateRolloutRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **createRolloutRequest** | [**CreateRolloutRequest**](CreateRolloutRequest.md) |  | 

### Return type

[**Rollout**](Rollout.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteRollout

> DeleteRollout(ctx, namespaceKey, flagKey, id).Execute()



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
	id := "id_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.RolloutsServiceAPI.DeleteRollout(context.Background(), namespaceKey, flagKey, id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolloutsServiceAPI.DeleteRollout``: %v\n", err)
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

Other parameters are passed through a pointer to a apiDeleteRolloutRequest struct via the builder pattern


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


## GetRollout

> Rollout GetRollout(ctx, namespaceKey, flagKey, id).Reference(reference).Execute()



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
	id := "id_example" // string | 
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RolloutsServiceAPI.GetRollout(context.Background(), namespaceKey, flagKey, id).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolloutsServiceAPI.GetRollout``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRollout`: Rollout
	fmt.Fprintf(os.Stdout, "Response from `RolloutsServiceAPI.GetRollout`: %v\n", resp)
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

Other parameters are passed through a pointer to a apiGetRolloutRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **reference** | **string** |  | 

### Return type

[**Rollout**](Rollout.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListRollouts

> RolloutList ListRollouts(ctx, namespaceKey, flagKey).Limit(limit).PageToken(pageToken).Reference(reference).Execute()



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
	limit := int32(56) // int32 |  (optional)
	pageToken := "pageToken_example" // string |  (optional)
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RolloutsServiceAPI.ListRollouts(context.Background(), namespaceKey, flagKey).Limit(limit).PageToken(pageToken).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolloutsServiceAPI.ListRollouts``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListRollouts`: RolloutList
	fmt.Fprintf(os.Stdout, "Response from `RolloutsServiceAPI.ListRollouts`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**flagKey** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListRolloutsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** |  | 
 **pageToken** | **string** |  | 
 **reference** | **string** |  | 

### Return type

[**RolloutList**](RolloutList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## OrderRollouts

> OrderRollouts(ctx, namespaceKey, flagKey).OrderRolloutsRequest(orderRolloutsRequest).Execute()



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
	orderRolloutsRequest := *openapiclient.NewOrderRolloutsRequest([]string{"RolloutIds_example"}) // OrderRolloutsRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.RolloutsServiceAPI.OrderRollouts(context.Background(), namespaceKey, flagKey).OrderRolloutsRequest(orderRolloutsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolloutsServiceAPI.OrderRollouts``: %v\n", err)
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

### Other Parameters

Other parameters are passed through a pointer to a apiOrderRolloutsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **orderRolloutsRequest** | [**OrderRolloutsRequest**](OrderRolloutsRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateRollout

> Rollout UpdateRollout(ctx, namespaceKey, flagKey, id).UpdateRolloutRequest(updateRolloutRequest).Execute()



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
	id := "id_example" // string | 
	updateRolloutRequest := *openapiclient.NewUpdateRolloutRequest() // UpdateRolloutRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RolloutsServiceAPI.UpdateRollout(context.Background(), namespaceKey, flagKey, id).UpdateRolloutRequest(updateRolloutRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RolloutsServiceAPI.UpdateRollout``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateRollout`: Rollout
	fmt.Fprintf(os.Stdout, "Response from `RolloutsServiceAPI.UpdateRollout`: %v\n", resp)
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

Other parameters are passed through a pointer to a apiUpdateRolloutRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **updateRolloutRequest** | [**UpdateRolloutRequest**](UpdateRolloutRequest.md) |  | 

### Return type

[**Rollout**](Rollout.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

