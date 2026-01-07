# \FliptAPI

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateConstraint**](FliptAPI.md#CreateConstraint) | **Post** /api/v1/namespaces/{namespaceKey}/segments/{segmentKey}/constraints | 
[**CreateDistribution**](FliptAPI.md#CreateDistribution) | **Post** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{ruleId}/distributions | 
[**CreateFlag**](FliptAPI.md#CreateFlag) | **Post** /api/v1/namespaces/{namespaceKey}/flags | 
[**CreateNamespace**](FliptAPI.md#CreateNamespace) | **Post** /api/v1/namespaces | 
[**CreateRollout**](FliptAPI.md#CreateRollout) | **Post** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts | 
[**CreateRule**](FliptAPI.md#CreateRule) | **Post** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules | 
[**CreateSegment**](FliptAPI.md#CreateSegment) | **Post** /api/v1/namespaces/{namespaceKey}/segments | 
[**CreateVariant**](FliptAPI.md#CreateVariant) | **Post** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/variants | 
[**DeleteConstraint**](FliptAPI.md#DeleteConstraint) | **Delete** /api/v1/namespaces/{namespaceKey}/segments/{segmentKey}/constraints/{id} | 
[**DeleteDistribution**](FliptAPI.md#DeleteDistribution) | **Delete** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{ruleId}/distributions/{id} | 
[**DeleteFlag**](FliptAPI.md#DeleteFlag) | **Delete** /api/v1/namespaces/{namespaceKey}/flags/{key} | 
[**DeleteNamespace**](FliptAPI.md#DeleteNamespace) | **Delete** /api/v1/namespaces/{key} | 
[**DeleteRollout**](FliptAPI.md#DeleteRollout) | **Delete** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts/{id} | 
[**DeleteRule**](FliptAPI.md#DeleteRule) | **Delete** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{id} | 
[**DeleteSegment**](FliptAPI.md#DeleteSegment) | **Delete** /api/v1/namespaces/{namespaceKey}/segments/{key} | 
[**DeleteVariant**](FliptAPI.md#DeleteVariant) | **Delete** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/variants/{id} | 
[**GetFlag**](FliptAPI.md#GetFlag) | **Get** /api/v1/namespaces/{namespaceKey}/flags/{key} | 
[**GetNamespace**](FliptAPI.md#GetNamespace) | **Get** /api/v1/namespaces/{key} | 
[**GetRollout**](FliptAPI.md#GetRollout) | **Get** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts/{id} | 
[**GetRule**](FliptAPI.md#GetRule) | **Get** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{id} | 
[**GetSegment**](FliptAPI.md#GetSegment) | **Get** /api/v1/namespaces/{namespaceKey}/segments/{key} | 
[**ListFlags**](FliptAPI.md#ListFlags) | **Get** /api/v1/namespaces/{namespaceKey}/flags | 
[**ListNamespaces**](FliptAPI.md#ListNamespaces) | **Get** /api/v1/namespaces | 
[**ListRollouts**](FliptAPI.md#ListRollouts) | **Get** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts | 
[**ListRules**](FliptAPI.md#ListRules) | **Get** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules | 
[**ListSegments**](FliptAPI.md#ListSegments) | **Get** /api/v1/namespaces/{namespaceKey}/segments | 
[**OrderRollouts**](FliptAPI.md#OrderRollouts) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts/order | 
[**OrderRules**](FliptAPI.md#OrderRules) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/order | 
[**UpdateConstraint**](FliptAPI.md#UpdateConstraint) | **Put** /api/v1/namespaces/{namespaceKey}/segments/{segmentKey}/constraints/{id} | 
[**UpdateDistribution**](FliptAPI.md#UpdateDistribution) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{ruleId}/distributions/{id} | 
[**UpdateFlag**](FliptAPI.md#UpdateFlag) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{key} | 
[**UpdateNamespace**](FliptAPI.md#UpdateNamespace) | **Put** /api/v1/namespaces/{key} | 
[**UpdateRollout**](FliptAPI.md#UpdateRollout) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rollouts/{id} | 
[**UpdateRule**](FliptAPI.md#UpdateRule) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/rules/{id} | 
[**UpdateSegment**](FliptAPI.md#UpdateSegment) | **Put** /api/v1/namespaces/{namespaceKey}/segments/{key} | 
[**UpdateVariant**](FliptAPI.md#UpdateVariant) | **Put** /api/v1/namespaces/{namespaceKey}/flags/{flagKey}/variants/{id} | 



## CreateConstraint

> Constraint CreateConstraint(ctx, namespaceKey, segmentKey).CreateConstraintRequest(createConstraintRequest).Execute()



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
	segmentKey := "segmentKey_example" // string | 
	createConstraintRequest := *openapiclient.NewCreateConstraintRequest("Type_example", "Property_example", "Operator_example") // CreateConstraintRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FliptAPI.CreateConstraint(context.Background(), namespaceKey, segmentKey).CreateConstraintRequest(createConstraintRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.CreateConstraint``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateConstraint`: Constraint
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.CreateConstraint`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.CreateDistribution(context.Background(), namespaceKey, flagKey, ruleId).CreateDistributionRequest(createDistributionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.CreateDistribution``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateDistribution`: Distribution
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.CreateDistribution`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.CreateFlag(context.Background(), namespaceKey).CreateFlagRequest(createFlagRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.CreateFlag``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateFlag`: Flag
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.CreateFlag`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.CreateNamespace(context.Background()).CreateNamespaceRequest(createNamespaceRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.CreateNamespace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateNamespace`: Namespace
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.CreateNamespace`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.CreateRollout(context.Background(), namespaceKey, flagKey).CreateRolloutRequest(createRolloutRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.CreateRollout``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateRollout`: Rollout
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.CreateRollout`: %v\n", resp)
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


## CreateRule

> Rule CreateRule(ctx, namespaceKey, flagKey).CreateRuleRequest(createRuleRequest).Execute()



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
	createRuleRequest := *openapiclient.NewCreateRuleRequest(int32(123)) // CreateRuleRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FliptAPI.CreateRule(context.Background(), namespaceKey, flagKey).CreateRuleRequest(createRuleRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.CreateRule``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateRule`: Rule
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.CreateRule`: %v\n", resp)
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


## CreateSegment

> Segment CreateSegment(ctx, namespaceKey).CreateSegmentRequest(createSegmentRequest).Execute()



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
	createSegmentRequest := *openapiclient.NewCreateSegmentRequest("Key_example", "Name_example", "MatchType_example") // CreateSegmentRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FliptAPI.CreateSegment(context.Background(), namespaceKey).CreateSegmentRequest(createSegmentRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.CreateSegment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateSegment`: Segment
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.CreateSegment`: %v\n", resp)
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


## CreateVariant

> Variant CreateVariant(ctx, namespaceKey, flagKey).CreateVariantRequest(createVariantRequest).Execute()



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
	createVariantRequest := *openapiclient.NewCreateVariantRequest("Key_example") // CreateVariantRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FliptAPI.CreateVariant(context.Background(), namespaceKey, flagKey).CreateVariantRequest(createVariantRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.CreateVariant``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateVariant`: Variant
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.CreateVariant`: %v\n", resp)
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


## DeleteConstraint

> DeleteConstraint(ctx, namespaceKey, segmentKey, id).Execute()



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
	segmentKey := "segmentKey_example" // string | 
	id := "id_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FliptAPI.DeleteConstraint(context.Background(), namespaceKey, segmentKey, id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.DeleteConstraint``: %v\n", err)
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
	r, err := apiClient.FliptAPI.DeleteDistribution(context.Background(), namespaceKey, flagKey, ruleId, id).VariantId(variantId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.DeleteDistribution``: %v\n", err)
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
	r, err := apiClient.FliptAPI.DeleteFlag(context.Background(), namespaceKey, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.DeleteFlag``: %v\n", err)
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
	r, err := apiClient.FliptAPI.DeleteNamespace(context.Background(), key).Force(force).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.DeleteNamespace``: %v\n", err)
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
	r, err := apiClient.FliptAPI.DeleteRollout(context.Background(), namespaceKey, flagKey, id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.DeleteRollout``: %v\n", err)
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


## DeleteRule

> DeleteRule(ctx, namespaceKey, flagKey, id).Execute()



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
	r, err := apiClient.FliptAPI.DeleteRule(context.Background(), namespaceKey, flagKey, id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.DeleteRule``: %v\n", err)
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


## DeleteSegment

> DeleteSegment(ctx, namespaceKey, key).Execute()



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
	r, err := apiClient.FliptAPI.DeleteSegment(context.Background(), namespaceKey, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.DeleteSegment``: %v\n", err)
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


## DeleteVariant

> DeleteVariant(ctx, namespaceKey, flagKey, id).Execute()



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
	r, err := apiClient.FliptAPI.DeleteVariant(context.Background(), namespaceKey, flagKey, id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.DeleteVariant``: %v\n", err)
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
	resp, r, err := apiClient.FliptAPI.GetFlag(context.Background(), namespaceKey, key).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.GetFlag``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFlag`: Flag
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.GetFlag`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.GetNamespace(context.Background(), key).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.GetNamespace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetNamespace`: Namespace
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.GetNamespace`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.GetRollout(context.Background(), namespaceKey, flagKey, id).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.GetRollout``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRollout`: Rollout
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.GetRollout`: %v\n", resp)
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


## GetRule

> Rule GetRule(ctx, namespaceKey, flagKey, id).Reference(reference).Execute()



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
	resp, r, err := apiClient.FliptAPI.GetRule(context.Background(), namespaceKey, flagKey, id).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.GetRule``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRule`: Rule
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.GetRule`: %v\n", resp)
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


## GetSegment

> Segment GetSegment(ctx, namespaceKey, key).Reference(reference).Execute()



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
	resp, r, err := apiClient.FliptAPI.GetSegment(context.Background(), namespaceKey, key).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.GetSegment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSegment`: Segment
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.GetSegment`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.ListFlags(context.Background(), namespaceKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.ListFlags``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListFlags`: FlagList
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.ListFlags`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.ListNamespaces(context.Background()).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.ListNamespaces``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListNamespaces`: NamespaceList
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.ListNamespaces`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.ListRollouts(context.Background(), namespaceKey, flagKey).Limit(limit).PageToken(pageToken).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.ListRollouts``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListRollouts`: RolloutList
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.ListRollouts`: %v\n", resp)
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


## ListRules

> RuleList ListRules(ctx, namespaceKey, flagKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()



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
	offset := int32(56) // int32 |  (optional)
	pageToken := "pageToken_example" // string |  (optional)
	reference := "reference_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FliptAPI.ListRules(context.Background(), namespaceKey, flagKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.ListRules``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListRules`: RuleList
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.ListRules`: %v\n", resp)
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


## ListSegments

> SegmentList ListSegments(ctx, namespaceKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()



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
	resp, r, err := apiClient.FliptAPI.ListSegments(context.Background(), namespaceKey).Limit(limit).Offset(offset).PageToken(pageToken).Reference(reference).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.ListSegments``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSegments`: SegmentList
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.ListSegments`: %v\n", resp)
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
	r, err := apiClient.FliptAPI.OrderRollouts(context.Background(), namespaceKey, flagKey).OrderRolloutsRequest(orderRolloutsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.OrderRollouts``: %v\n", err)
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


## OrderRules

> OrderRules(ctx, namespaceKey, flagKey).OrderRulesRequest(orderRulesRequest).Execute()



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
	orderRulesRequest := *openapiclient.NewOrderRulesRequest([]string{"RuleIds_example"}) // OrderRulesRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FliptAPI.OrderRules(context.Background(), namespaceKey, flagKey).OrderRulesRequest(orderRulesRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.OrderRules``: %v\n", err)
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


## UpdateConstraint

> Constraint UpdateConstraint(ctx, namespaceKey, segmentKey, id).UpdateConstraintRequest(updateConstraintRequest).Execute()



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
	segmentKey := "segmentKey_example" // string | 
	id := "id_example" // string | 
	updateConstraintRequest := *openapiclient.NewUpdateConstraintRequest("Type_example", "Property_example", "Operator_example") // UpdateConstraintRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FliptAPI.UpdateConstraint(context.Background(), namespaceKey, segmentKey, id).UpdateConstraintRequest(updateConstraintRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.UpdateConstraint``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateConstraint`: Constraint
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.UpdateConstraint`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.UpdateDistribution(context.Background(), namespaceKey, flagKey, ruleId, id).UpdateDistributionRequest(updateDistributionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.UpdateDistribution``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateDistribution`: Distribution
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.UpdateDistribution`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.UpdateFlag(context.Background(), namespaceKey, key).UpdateFlagRequest(updateFlagRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.UpdateFlag``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateFlag`: Flag
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.UpdateFlag`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.UpdateNamespace(context.Background(), key).UpdateNamespaceRequest(updateNamespaceRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.UpdateNamespace``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateNamespace`: Namespace
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.UpdateNamespace`: %v\n", resp)
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
	resp, r, err := apiClient.FliptAPI.UpdateRollout(context.Background(), namespaceKey, flagKey, id).UpdateRolloutRequest(updateRolloutRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.UpdateRollout``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateRollout`: Rollout
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.UpdateRollout`: %v\n", resp)
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


## UpdateRule

> Rule UpdateRule(ctx, namespaceKey, flagKey, id).UpdateRuleRequest(updateRuleRequest).Execute()



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
	updateRuleRequest := *openapiclient.NewUpdateRuleRequest() // UpdateRuleRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FliptAPI.UpdateRule(context.Background(), namespaceKey, flagKey, id).UpdateRuleRequest(updateRuleRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.UpdateRule``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateRule`: Rule
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.UpdateRule`: %v\n", resp)
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


## UpdateSegment

> Segment UpdateSegment(ctx, namespaceKey, key).UpdateSegmentRequest(updateSegmentRequest).Execute()



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
	updateSegmentRequest := *openapiclient.NewUpdateSegmentRequest("Name_example", "MatchType_example") // UpdateSegmentRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FliptAPI.UpdateSegment(context.Background(), namespaceKey, key).UpdateSegmentRequest(updateSegmentRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.UpdateSegment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateSegment`: Segment
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.UpdateSegment`: %v\n", resp)
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


## UpdateVariant

> Variant UpdateVariant(ctx, namespaceKey, flagKey, id).UpdateVariantRequest(updateVariantRequest).Execute()



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
	updateVariantRequest := *openapiclient.NewUpdateVariantRequest("Key_example") // UpdateVariantRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FliptAPI.UpdateVariant(context.Background(), namespaceKey, flagKey, id).UpdateVariantRequest(updateVariantRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FliptAPI.UpdateVariant``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateVariant`: Variant
	fmt.Fprintf(os.Stdout, "Response from `FliptAPI.UpdateVariant`: %v\n", resp)
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

