# \SegmentsServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateSegment**](SegmentsServiceAPI.md#CreateSegment) | **Post** /api/v1/namespaces/{namespaceKey}/segments | 
[**DeleteSegment**](SegmentsServiceAPI.md#DeleteSegment) | **Delete** /api/v1/namespaces/{namespaceKey}/segments/{key} | 
[**GetSegment**](SegmentsServiceAPI.md#GetSegment) | **Get** /api/v1/namespaces/{namespaceKey}/segments/{key} | 
[**ListSegments**](SegmentsServiceAPI.md#ListSegments) | **Get** /api/v1/namespaces/{namespaceKey}/segments | 
[**UpdateSegment**](SegmentsServiceAPI.md#UpdateSegment) | **Put** /api/v1/namespaces/{namespaceKey}/segments/{key} | 



## CreateSegment

> Segment CreateSegment(ctx, namespaceKey).CreateSegmentRequest(createSegmentRequest).Execute()



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
	createSegmentRequest := *openapiclient.NewCreateSegmentRequest("Key_example", "Name_example", "MatchType_example") // CreateSegmentRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SegmentsServiceAPI.CreateSegment(context.Background(), namespaceKey).CreateSegmentRequest(createSegmentRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SegmentsServiceAPI.CreateSegment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateSegment`: Segment
	fmt.Fprintf(os.Stdout, "Response from `SegmentsServiceAPI.CreateSegment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateSegmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createSegmentRequest** | [**CreateSegmentRequest**](CreateSegmentRequest.md) |  | 

### Return type

[**Segment**](Segment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteSegment

> DeleteSegment(ctx, namespaceKey, key).Execute()



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
	key := "key_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.SegmentsServiceAPI.DeleteSegment(context.Background(), namespaceKey, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SegmentsServiceAPI.DeleteSegment``: %v\n", err)
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

Other parameters are passed through a pointer to a apiDeleteSegmentRequest struct via the builder pattern


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


## GetSegment

> Segment GetSegment(ctx, namespaceKey, key).Reference(reference).Execute()



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
	key := "key_example" // string | 
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SegmentsServiceAPI.GetSegment(context.Background(), namespaceKey, key).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SegmentsServiceAPI.GetSegment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSegment`: Segment
	fmt.Fprintf(os.Stdout, "Response from `SegmentsServiceAPI.GetSegment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**key** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSegmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **reference** | **string** |  | 

### Return type

[**Segment**](Segment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSegments

> SegmentList ListSegments(ctx, namespaceKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()



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
	limit := int32(56) // int32 |  (optional)
	offset := int32(56) // int32 |  (optional)
	pageToken := "pageToken_example" // string |  (optional)
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SegmentsServiceAPI.ListSegments(context.Background(), namespaceKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SegmentsServiceAPI.ListSegments``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSegments`: SegmentList
	fmt.Fprintf(os.Stdout, "Response from `SegmentsServiceAPI.ListSegments`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListSegmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** |  | 
 **offset** | **int32** |  | 
 **pageToken** | **string** |  | 
 **reference** | **string** |  | 

### Return type

[**SegmentList**](SegmentList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateSegment

> Segment UpdateSegment(ctx, namespaceKey, key).UpdateSegmentRequest(updateSegmentRequest).Execute()



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
	key := "key_example" // string | 
	updateSegmentRequest := *openapiclient.NewUpdateSegmentRequest("Name_example", "MatchType_example") // UpdateSegmentRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SegmentsServiceAPI.UpdateSegment(context.Background(), namespaceKey, key).UpdateSegmentRequest(updateSegmentRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SegmentsServiceAPI.UpdateSegment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateSegment`: Segment
	fmt.Fprintf(os.Stdout, "Response from `SegmentsServiceAPI.UpdateSegment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**key** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateSegmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **updateSegmentRequest** | [**UpdateSegmentRequest**](UpdateSegmentRequest.md) |  | 

### Return type

[**Segment**](Segment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

