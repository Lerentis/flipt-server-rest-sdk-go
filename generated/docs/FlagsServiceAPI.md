# \FlagsServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateFlag**](FlagsServiceAPI.md#CreateFlag) | **Post** /api/v1/namespaces/{namespaceKey}/flags | 
[**DeleteFlag**](FlagsServiceAPI.md#DeleteFlag) | **Delete** /api/v1/namespaces/{namespaceKey}/flags/{key} | 
[**GetFlag**](FlagsServiceAPI.md#GetFlag) | **Get** /api/v1/namespaces/{namespaceKey}/flags/{key} | 
[**ListFlags**](FlagsServiceAPI.md#ListFlags) | **Get** /api/v1/namespaces/{namespaceKey}/flags | 
[**UpdateFlag**](FlagsServiceAPI.md#UpdateFlag) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{key} | 



## CreateFlag

> Flag CreateFlag(ctx, namespaceKey).CreateFlagRequest(createFlagRequest).Execute()



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
	createFlagRequest := *openapiclient.NewCreateFlagRequest("Key_example", "Name_example", "Type_example") // CreateFlagRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlagsServiceAPI.CreateFlag(context.Background(), namespaceKey).CreateFlagRequest(createFlagRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlagsServiceAPI.CreateFlag``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateFlag`: Flag
	fmt.Fprintf(os.Stdout, "Response from `FlagsServiceAPI.CreateFlag`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateFlagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createFlagRequest** | [**CreateFlagRequest**](CreateFlagRequest.md) |  | 

### Return type

[**Flag**](Flag.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteFlag

> DeleteFlag(ctx, namespaceKey, key).Execute()



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
	key := "key_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FlagsServiceAPI.DeleteFlag(context.Background(), namespaceKey, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlagsServiceAPI.DeleteFlag``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**key** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteFlagRequest struct via the builder pattern


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


## GetFlag

> Flag GetFlag(ctx, namespaceKey, key).Reference(reference).Execute()



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
	key := "key_example" // string | 
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlagsServiceAPI.GetFlag(context.Background(), namespaceKey, key).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlagsServiceAPI.GetFlag``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFlag`: Flag
	fmt.Fprintf(os.Stdout, "Response from `FlagsServiceAPI.GetFlag`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**key** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetFlagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **reference** | **string** |  | 

### Return type

[**Flag**](Flag.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListFlags

> FlagList ListFlags(ctx, namespaceKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()



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
	limit := int32(56) // int32 |  (optional)
	offset := int32(56) // int32 |  (optional)
	pageToken := "pageToken_example" // string |  (optional)
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlagsServiceAPI.ListFlags(context.Background(), namespaceKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlagsServiceAPI.ListFlags``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListFlags`: FlagList
	fmt.Fprintf(os.Stdout, "Response from `FlagsServiceAPI.ListFlags`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListFlagsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** |  | 
 **offset** | **int32** |  | 
 **pageToken** | **string** |  | 
 **reference** | **string** |  | 

### Return type

[**FlagList**](FlagList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateFlag

> Flag UpdateFlag(ctx, namespaceKey, key).UpdateFlagRequest(updateFlagRequest).Execute()



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
	key := "key_example" // string | 
	updateFlagRequest := *openapiclient.NewUpdateFlagRequest("Name_example") // UpdateFlagRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FlagsServiceAPI.UpdateFlag(context.Background(), namespaceKey, key).UpdateFlagRequest(updateFlagRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FlagsServiceAPI.UpdateFlag``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateFlag`: Flag
	fmt.Fprintf(os.Stdout, "Response from `FlagsServiceAPI.UpdateFlag`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**key** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateFlagRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **updateFlagRequest** | [**UpdateFlagRequest**](UpdateFlagRequest.md) |  | 

### Return type

[**Flag**](Flag.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

