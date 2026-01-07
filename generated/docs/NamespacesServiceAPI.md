# \NamespacesServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateNamespace**](NamespacesServiceAPI.md#CreateNamespace) | **Post** /api/v1/namespaces | 
[**DeleteNamespace**](NamespacesServiceAPI.md#DeleteNamespace) | **Delete** /api/v1/namespaces/{key} | 
[**GetNamespace**](NamespacesServiceAPI.md#GetNamespace) | **Get** /api/v1/namespaces/{key} | 
[**ListNamespaces**](NamespacesServiceAPI.md#ListNamespaces) | **Get** /api/v1/namespaces | 
[**UpdateNamespace**](NamespacesServiceAPI.md#UpdateNamespace) | **Put** /api/v1/namespaces/{key} | 



## CreateNamespace

> Namespace CreateNamespace(ctx).CreateNamespaceRequest(createNamespaceRequest).Execute()



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
	createNamespaceRequest := *openapiclient.NewCreateNamespaceRequest("Key_example", "Name_example") // CreateNamespaceRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NamespacesServiceAPI.CreateNamespace(context.Background()).CreateNamespaceRequest(createNamespaceRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NamespacesServiceAPI.CreateNamespace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateNamespace`: Namespace
	fmt.Fprintf(os.Stdout, "Response from `NamespacesServiceAPI.CreateNamespace`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateNamespaceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createNamespaceRequest** | [**CreateNamespaceRequest**](CreateNamespaceRequest.md) |  | 

### Return type

[**Namespace**](Namespace.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteNamespace

> DeleteNamespace(ctx, key).Force(force).Execute()



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
	key := "key_example" // string | 
	force := true // bool |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.NamespacesServiceAPI.DeleteNamespace(context.Background(), key).Force(force).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NamespacesServiceAPI.DeleteNamespace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**key** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteNamespaceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **force** | **bool** |  | 

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


## GetNamespace

> Namespace GetNamespace(ctx, key).Reference(reference).Execute()



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
	key := "key_example" // string | 
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NamespacesServiceAPI.GetNamespace(context.Background(), key).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NamespacesServiceAPI.GetNamespace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetNamespace`: Namespace
	fmt.Fprintf(os.Stdout, "Response from `NamespacesServiceAPI.GetNamespace`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**key** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetNamespaceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **reference** | **string** |  | 

### Return type

[**Namespace**](Namespace.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListNamespaces

> NamespaceList ListNamespaces(ctx).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()



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
	limit := int32(56) // int32 |  (optional)
	offset := int32(56) // int32 |  (optional)
	pageToken := "pageToken_example" // string |  (optional)
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NamespacesServiceAPI.ListNamespaces(context.Background()).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NamespacesServiceAPI.ListNamespaces``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListNamespaces`: NamespaceList
	fmt.Fprintf(os.Stdout, "Response from `NamespacesServiceAPI.ListNamespaces`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListNamespacesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** |  | 
 **offset** | **int32** |  | 
 **pageToken** | **string** |  | 
 **reference** | **string** |  | 

### Return type

[**NamespaceList**](NamespaceList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateNamespace

> Namespace UpdateNamespace(ctx, key).UpdateNamespaceRequest(updateNamespaceRequest).Execute()



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
	key := "key_example" // string | 
	updateNamespaceRequest := *openapiclient.NewUpdateNamespaceRequest("Name_example") // UpdateNamespaceRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NamespacesServiceAPI.UpdateNamespace(context.Background(), key).UpdateNamespaceRequest(updateNamespaceRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NamespacesServiceAPI.UpdateNamespace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateNamespace`: Namespace
	fmt.Fprintf(os.Stdout, "Response from `NamespacesServiceAPI.UpdateNamespace`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**key** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateNamespaceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateNamespaceRequest** | [**UpdateNamespaceRequest**](UpdateNamespaceRequest.md) |  | 

### Return type

[**Namespace**](Namespace.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

