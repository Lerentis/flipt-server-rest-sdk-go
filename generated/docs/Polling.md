# Polling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | Pointer to **bool** |  | [optional] 
**MinPollingIntervalMs** | Pointer to **int32** |  | [optional] 

## Methods

### NewPolling

`func NewPolling() *Polling`

NewPolling instantiates a new Polling object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPollingWithDefaults

`func NewPollingWithDefaults() *Polling`

NewPollingWithDefaults instantiates a new Polling object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *Polling) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *Polling) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *Polling) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *Polling) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetMinPollingIntervalMs

`func (o *Polling) GetMinPollingIntervalMs() int32`

GetMinPollingIntervalMs returns the MinPollingIntervalMs field if non-nil, zero value otherwise.

### GetMinPollingIntervalMsOk

`func (o *Polling) GetMinPollingIntervalMsOk() (*int32, bool)`

GetMinPollingIntervalMsOk returns a tuple with the MinPollingIntervalMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinPollingIntervalMs

`func (o *Polling) SetMinPollingIntervalMs(v int32)`

SetMinPollingIntervalMs sets MinPollingIntervalMs field to given value.

### HasMinPollingIntervalMs

`func (o *Polling) HasMinPollingIntervalMs() bool`

HasMinPollingIntervalMs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


