# \ConstraintsServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateConstraint**](ConstraintsServiceAPI.md#CreateConstraint) | **Post** /api/v1/namespaces/{namespaceKey}/segments/{segmentKey}/constraints | 
[**DeleteConstraint**](ConstraintsServiceAPI.md#DeleteConstraint) | **Delete** /api/v1/namespaces/{namespaceKey}/segments/{segmentKey}/constraints/{id} | 
[**UpdateConstraint**](ConstraintsServiceAPI.md#UpdateConstraint) | **Put** /api/v1/namespaces/{namespaceKey}/segments/{segmentKey}/constraints/{id} | 



## CreateConstraint

> Constraint CreateConstraint(ctx, namespaceKey, segmentKey).CreateConstraintRequest(createConstraintRequest).Execute()



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
	segmentKey := "segmentKey_example" // string | 
	createConstraintRequest := *openapiclient.NewCreateConstraintRequest("Type_example", "Property_example", "Operator_example") // CreateConstraintRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ConstraintsServiceAPI.CreateConstraint(context.Background(), namespaceKey, segmentKey).CreateConstraintRequest(createConstraintRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConstraintsServiceAPI.CreateConstraint``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateConstraint`: Constraint
	fmt.Fprintf(os.Stdout, "Response from `ConstraintsServiceAPI.CreateConstraint`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**segmentKey** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateConstraintRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **createConstraintRequest** | [**CreateConstraintRequest**](CreateConstraintRequest.md) |  | 

### Return type

[**Constraint**](Constraint.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteConstraint

> DeleteConstraint(ctx, namespaceKey, segmentKey, id).Execute()



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
	segmentKey := "segmentKey_example" // string | 
	id := "id_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ConstraintsServiceAPI.DeleteConstraint(context.Background(), namespaceKey, segmentKey, id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConstraintsServiceAPI.DeleteConstraint``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**segmentKey** | **string** |  | 
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteConstraintRequest struct via the builder pattern


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


## UpdateConstraint

> Constraint UpdateConstraint(ctx, namespaceKey, segmentKey, id).UpdateConstraintRequest(updateConstraintRequest).Execute()



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
	segmentKey := "segmentKey_example" // string | 
	id := "id_example" // string | 
	updateConstraintRequest := *openapiclient.NewUpdateConstraintRequest("Type_example", "Property_example", "Operator_example") // UpdateConstraintRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ConstraintsServiceAPI.UpdateConstraint(context.Background(), namespaceKey, segmentKey, id).UpdateConstraintRequest(updateConstraintRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ConstraintsServiceAPI.UpdateConstraint``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateConstraint`: Constraint
	fmt.Fprintf(os.Stdout, "Response from `ConstraintsServiceAPI.UpdateConstraint`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**segmentKey** | **string** |  | 
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateConstraintRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **updateConstraintRequest** | [**UpdateConstraintRequest**](UpdateConstraintRequest.md) |  | 

### Return type

[**Constraint**](Constraint.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

