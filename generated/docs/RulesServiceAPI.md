# \RulesServiceAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateRule**](RulesServiceAPI.md#CreateRule) | **Post** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules | 
[**DeleteRule**](RulesServiceAPI.md#DeleteRule) | **Delete** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{id} | 
[**GetRule**](RulesServiceAPI.md#GetRule) | **Get** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{id} | 
[**ListRules**](RulesServiceAPI.md#ListRules) | **Get** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules | 
[**OrderRules**](RulesServiceAPI.md#OrderRules) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/order | 
[**UpdateRule**](RulesServiceAPI.md#UpdateRule) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{id} | 



## CreateRule

> Rule CreateRule(ctx, namespaceKey, flagKey).CreateRuleRequest(createRuleRequest).Execute()



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
	createRuleRequest := *openapiclient.NewCreateRuleRequest(int32(123)) // CreateRuleRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RulesServiceAPI.CreateRule(context.Background(), namespaceKey, flagKey).CreateRuleRequest(createRuleRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RulesServiceAPI.CreateRule``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateRule`: Rule
	fmt.Fprintf(os.Stdout, "Response from `RulesServiceAPI.CreateRule`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**flagKey** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateRuleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **createRuleRequest** | [**CreateRuleRequest**](CreateRuleRequest.md) |  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteRule

> DeleteRule(ctx, namespaceKey, flagKey, id).Execute()



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
	r, err := apiClient.RulesServiceAPI.DeleteRule(context.Background(), namespaceKey, flagKey, id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RulesServiceAPI.DeleteRule``: %v\n", err)
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

Other parameters are passed through a pointer to a apiDeleteRuleRequest struct via the builder pattern


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


## GetRule

> Rule GetRule(ctx, namespaceKey, flagKey, id).Reference(reference).Execute()



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
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RulesServiceAPI.GetRule(context.Background(), namespaceKey, flagKey, id).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RulesServiceAPI.GetRule``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRule`: Rule
	fmt.Fprintf(os.Stdout, "Response from `RulesServiceAPI.GetRule`: %v\n", resp)
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

Other parameters are passed through a pointer to a apiGetRuleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **reference** | **string** |  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListRules

> RuleList ListRules(ctx, namespaceKey, flagKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()



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
	limit := int32(56) // int32 |  (optional)
	offset := int32(56) // int32 |  (optional)
	pageToken := "pageToken_example" // string |  (optional)
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RulesServiceAPI.ListRules(context.Background(), namespaceKey, flagKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RulesServiceAPI.ListRules``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListRules`: RuleList
	fmt.Fprintf(os.Stdout, "Response from `RulesServiceAPI.ListRules`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**namespaceKey** | **string** |  | 
**flagKey** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListRulesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** |  | 
 **offset** | **int32** |  | 
 **pageToken** | **string** |  | 
 **reference** | **string** |  | 

### Return type

[**RuleList**](RuleList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## OrderRules

> OrderRules(ctx, namespaceKey, flagKey).OrderRulesRequest(orderRulesRequest).Execute()



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
	orderRulesRequest := *openapiclient.NewOrderRulesRequest([]string{"RuleIds_example"}) // OrderRulesRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.RulesServiceAPI.OrderRules(context.Background(), namespaceKey, flagKey).OrderRulesRequest(orderRulesRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RulesServiceAPI.OrderRules``: %v\n", err)
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

Other parameters are passed through a pointer to a apiOrderRulesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **orderRulesRequest** | [**OrderRulesRequest**](OrderRulesRequest.md) |  | 

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


## UpdateRule

> Rule UpdateRule(ctx, namespaceKey, flagKey, id).UpdateRuleRequest(updateRuleRequest).Execute()



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
	updateRuleRequest := *openapiclient.NewUpdateRuleRequest() // UpdateRuleRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RulesServiceAPI.UpdateRule(context.Background(), namespaceKey, flagKey, id).UpdateRuleRequest(updateRuleRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RulesServiceAPI.UpdateRule``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateRule`: Rule
	fmt.Fprintf(os.Stdout, "Response from `RulesServiceAPI.UpdateRule`: %v\n", resp)
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

Other parameters are passed through a pointer to a apiUpdateRuleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **updateRuleRequest** | [**UpdateRuleRequest**](UpdateRuleRequest.md) |  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

