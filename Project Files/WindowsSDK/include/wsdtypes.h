//+-------------------------------------------------------------------------
//
//  Microsoft Windows
//  Copyright (c) Microsoft Corporation. All rights reserved.
//
//  Component: WSDAPI - Microsoft Web Services for Devices API
// 
//  File: wsdtypes.h
//
//  Abstract: WSDAPI Built-in Type Definitions
//
//  THIS FILE IS AUTOMATICALLY GENERATED.  DO NOT MODIFY IT BY HAND.
//
//--------------------------------------------------------------------------
#pragma once

//
// Forward definitions
//
interface IWSDMessageParameters;   // wsdbase.idl
interface IWSDServiceMessaging;    // wsdhost.idl

// decl referenced base types
typedef struct _WSD_DURATION WSD_DURATION;
typedef struct _WSD_DATETIME WSD_DATETIME;

typedef struct _WSD_HANDLER_CONTEXT WSD_HANDLER_CONTEXT;
typedef struct _WSD_EVENT WSD_EVENT;

typedef HRESULT (*WSD_STUB_FUNCTION) (   
    IUnknown* server,
    IWSDServiceMessaging* session,
    WSD_EVENT* event
);

typedef enum _WSD_PROTOCOL_TYPE
{
    WSD_PT_NONE  = 0x00,
    WSD_PT_UDP   = 0x01,
    WSD_PT_HTTP  = 0x02,
    WSD_PT_HTTPS = 0x04,
    WSD_PT_ALL   = 0xff,
} WSD_PROTOCOL_TYPE;

typedef struct _WSD_OPERATION
{
    WSDXML_TYPE* RequestType;
    WSDXML_TYPE* ResponseType;
    WSD_STUB_FUNCTION RequestStubFunction;
} WSD_OPERATION;

//
// Context for handling incoming messages.
//
typedef 
HRESULT (*PWSD_SOAP_MESSAGE_HANDLER)(
    IUnknown* thisUnknown,
    WSD_EVENT* event);

//
// Context for handling incoming messages.
//
struct _WSD_HANDLER_CONTEXT
{
    PWSD_SOAP_MESSAGE_HANDLER Handler;
    void* PVoid;
    IUnknown* Unknown;
};

//
// WSDEventType distinguishes types of events produced by the session layer.
//
typedef enum _WSDEventType
{
    WSDET_NONE                 = 0,
    WSDET_INCOMING_MESSAGE     = 1,
    WSDET_INCOMING_FAULT       = 2,
    WSDET_TRANSMISSION_FAILURE = 3,
    WSDET_RESPONSE_TIMEOUT     = 4,
} WSDEventType;

typedef struct _WSD_SYNCHRONOUS_RESPONSE_CONTEXT
{
    HRESULT hr;
    HANDLE eventHandle;
    IWSDMessageParameters* messageParameters;
    void* results;
} WSD_SYNCHRONOUS_RESPONSE_CONTEXT;

typedef struct _WSD_PORT_TYPE
{
    DWORD EncodedName;
    DWORD OperationCount;
    WSD_OPERATION* Operations;
    WSD_PROTOCOL_TYPE ProtocolType;
} WSD_PORT_TYPE;

        
typedef struct _WSD_RELATIONSHIP_METADATA WSD_RELATIONSHIP_METADATA;
typedef struct _WSD_SERVICE_METADATA_LIST WSD_SERVICE_METADATA_LIST;
typedef struct _WSD_HOST_METADATA WSD_HOST_METADATA;
typedef struct _WSD_ENDPOINT_REFERENCE_LIST WSD_ENDPOINT_REFERENCE_LIST;
typedef struct _WSD_SERVICE_METADATA WSD_SERVICE_METADATA;
typedef struct _WSD_EVENTING_DELIVERY_MODE_PUSH WSD_EVENTING_DELIVERY_MODE_PUSH;
typedef struct _WSD_EVENTING_FILTER_ACTION WSD_EVENTING_FILTER_ACTION;
typedef struct _WSD_THIS_DEVICE_METADATA WSD_THIS_DEVICE_METADATA;
typedef struct _WSD_THIS_MODEL_METADATA WSD_THIS_MODEL_METADATA;
typedef struct _WSD_LOCALIZED_STRING_LIST WSD_LOCALIZED_STRING_LIST;
typedef struct _WSD_SOAP_FAULT_REASON WSD_SOAP_FAULT_REASON;
typedef struct _WSD_SOAP_FAULT_SUBCODE WSD_SOAP_FAULT_SUBCODE;
typedef struct _WSD_SOAP_FAULT_CODE WSD_SOAP_FAULT_CODE;
typedef struct _WSD_SOAP_FAULT WSD_SOAP_FAULT;
typedef struct _WSD_APP_SEQUENCE WSD_APP_SEQUENCE;
typedef struct _WSD_HEADER_RELATESTO WSD_HEADER_RELATESTO;
typedef struct _WSD_SOAP_HEADER WSD_SOAP_HEADER;
typedef struct _WSD_SOAP_MESSAGE WSD_SOAP_MESSAGE;
typedef struct _WSD_RESOLVE_MATCHES WSD_RESOLVE_MATCHES;
typedef struct _WSD_RESOLVE_MATCH WSD_RESOLVE_MATCH;
typedef struct _WSD_RESOLVE WSD_RESOLVE;
typedef struct _WSD_PROBE_MATCH WSD_PROBE_MATCH;
typedef struct _WSD_PROBE_MATCH_LIST WSD_PROBE_MATCH_LIST;
typedef struct _WSD_PROBE_MATCHES WSD_PROBE_MATCHES;
typedef struct _WSD_PROBE WSD_PROBE;
typedef struct _WSD_BYE WSD_BYE;
typedef struct _WSD_URI_LIST WSD_URI_LIST;
typedef struct _WSD_SCOPES WSD_SCOPES;
typedef struct _WSD_NAME_LIST WSD_NAME_LIST;
typedef struct _WSD_HELLO WSD_HELLO;
typedef struct _WSD_REFERENCE_PARAMETERS WSD_REFERENCE_PARAMETERS;
typedef struct _WSD_REFERENCE_PROPERTIES WSD_REFERENCE_PROPERTIES;
typedef struct _WSD_ENDPOINT_REFERENCE WSD_ENDPOINT_REFERENCE;
typedef struct _WSD_METADATA_SECTION WSD_METADATA_SECTION;
typedef struct _WSD_METADATA_SECTION_LIST WSD_METADATA_SECTION_LIST;
typedef struct _WSD_EVENTING_FILTER WSD_EVENTING_FILTER;
typedef struct _WSD_EVENTING_EXPIRES WSD_EVENTING_EXPIRES;
typedef struct _WSD_EVENTING_DELIVERY_MODE WSD_EVENTING_DELIVERY_MODE;
typedef struct _WSD_LOCALIZED_STRING WSD_LOCALIZED_STRING;

// 
// Structure definition WSD_RELATIONSHIP_METADATA
// 
struct _WSD_RELATIONSHIP_METADATA
{
    const WCHAR* Type;
    WSD_HOST_METADATA* Data;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_SERVICE_METADATA_LIST
// 
struct _WSD_SERVICE_METADATA_LIST
{
    WSD_SERVICE_METADATA_LIST* Next;
    WSD_SERVICE_METADATA* Element;
};

// 
// Structure definition WSD_HOST_METADATA
// 
struct _WSD_HOST_METADATA
{
    WSD_SERVICE_METADATA* Host;
    WSD_SERVICE_METADATA_LIST* Hosted;
};

// 
// Structure definition WSD_ENDPOINT_REFERENCE_LIST
// 
struct _WSD_ENDPOINT_REFERENCE_LIST
{
    WSD_ENDPOINT_REFERENCE_LIST* Next;
    WSD_ENDPOINT_REFERENCE* Element;
};

// 
// Structure definition WSD_SERVICE_METADATA
// 
struct _WSD_SERVICE_METADATA
{
    WSD_ENDPOINT_REFERENCE_LIST* EndpointReference;
    WSD_NAME_LIST* Types;
    const WCHAR* ServiceId;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_EVENTING_DELIVERY_MODE_PUSH
// 
struct _WSD_EVENTING_DELIVERY_MODE_PUSH
{
    WSD_ENDPOINT_REFERENCE* NotifyTo;
};

// 
// Structure definition WSD_EVENTING_FILTER_ACTION
// 
struct _WSD_EVENTING_FILTER_ACTION
{
    WSD_URI_LIST* Actions;
};

// 
// Structure definition WSD_THIS_DEVICE_METADATA
// 
struct _WSD_THIS_DEVICE_METADATA
{
    WSD_LOCALIZED_STRING_LIST* FriendlyName;
    const WCHAR* FirmwareVersion;
    const WCHAR* SerialNumber;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_THIS_MODEL_METADATA
// 
struct _WSD_THIS_MODEL_METADATA
{
    WSD_LOCALIZED_STRING_LIST* Manufacturer;
    const WCHAR* ManufacturerUrl;
    WSD_LOCALIZED_STRING_LIST* ModelName;
    const WCHAR* ModelNumber;
    const WCHAR* ModelUrl;
    const WCHAR* PresentationUrl;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_LOCALIZED_STRING_LIST
// 
struct _WSD_LOCALIZED_STRING_LIST
{
    WSD_LOCALIZED_STRING_LIST* Next;
    WSD_LOCALIZED_STRING* Element;
};

// 
// Structure definition WSD_SOAP_FAULT_REASON
// 
struct _WSD_SOAP_FAULT_REASON
{
    WSD_LOCALIZED_STRING_LIST* Text;
};

// 
// Structure definition WSD_SOAP_FAULT_SUBCODE
// 
struct _WSD_SOAP_FAULT_SUBCODE
{
    WSDXML_NAME* Value;
    WSD_SOAP_FAULT_SUBCODE* Subcode;
};

// 
// Structure definition WSD_SOAP_FAULT_CODE
// 
struct _WSD_SOAP_FAULT_CODE
{
    WSDXML_NAME* Value;
    WSD_SOAP_FAULT_SUBCODE* Subcode;
};

// 
// Structure definition WSD_SOAP_FAULT
// 
struct _WSD_SOAP_FAULT
{
    WSD_SOAP_FAULT_CODE* Code;
    WSD_SOAP_FAULT_REASON* Reason;
    const WCHAR* Node;
    const WCHAR* Role;
    WSDXML_ELEMENT* Detail;
};

// 
// Structure definition WSD_APP_SEQUENCE
// 
struct _WSD_APP_SEQUENCE
{
    ULONGLONG InstanceId;
    const WCHAR* SequenceId;
    ULONGLONG MessageNumber;
};

// 
// Structure definition WSD_HEADER_RELATESTO
// 
struct _WSD_HEADER_RELATESTO
{
    WSDXML_NAME* RelationshipType;
    const WCHAR* MessageID;
};

// 
// Structure definition WSD_SOAP_HEADER
// 
struct _WSD_SOAP_HEADER
{
    const WCHAR* To;
    const WCHAR* Action;
    const WCHAR* MessageID;
    WSD_HEADER_RELATESTO RelatesTo;
    WSD_ENDPOINT_REFERENCE* ReplyTo;
    WSD_ENDPOINT_REFERENCE* From;
    WSD_ENDPOINT_REFERENCE* FaultTo;
    WSD_APP_SEQUENCE* AppSequence;
    WSDXML_ELEMENT* AnyHeaders;
};

// 
// Structure definition WSD_SOAP_MESSAGE
// 
struct _WSD_SOAP_MESSAGE
{
    WSD_SOAP_HEADER Header;
    void* Body;
    WSDXML_TYPE* BodyType;
};

// 
// Structure definition WSD_RESOLVE_MATCHES
// 
struct _WSD_RESOLVE_MATCHES
{
    WSD_RESOLVE_MATCH* ResolveMatch;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_RESOLVE_MATCH
// 
struct _WSD_RESOLVE_MATCH
{
    WSD_ENDPOINT_REFERENCE* EndpointReference;
    WSD_NAME_LIST* Types;
    WSD_SCOPES* Scopes;
    WSD_URI_LIST* XAddrs;
    ULONGLONG MetadataVersion;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_RESOLVE
// 
struct _WSD_RESOLVE
{
    WSD_ENDPOINT_REFERENCE* EndpointReference;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_PROBE_MATCH
// 
struct _WSD_PROBE_MATCH
{
    WSD_ENDPOINT_REFERENCE* EndpointReference;
    WSD_NAME_LIST* Types;
    WSD_SCOPES* Scopes;
    WSD_URI_LIST* XAddrs;
    ULONGLONG MetadataVersion;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_PROBE_MATCH_LIST
// 
struct _WSD_PROBE_MATCH_LIST
{
    WSD_PROBE_MATCH_LIST* Next;
    WSD_PROBE_MATCH* Element;
};

// 
// Structure definition WSD_PROBE_MATCHES
// 
struct _WSD_PROBE_MATCHES
{
    WSD_PROBE_MATCH_LIST* ProbeMatch;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_PROBE
// 
struct _WSD_PROBE
{
    WSD_NAME_LIST* Types;
    WSD_SCOPES* Scopes;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_BYE
// 
struct _WSD_BYE
{
    WSD_ENDPOINT_REFERENCE* EndpointReference;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_URI_LIST
// 
struct _WSD_URI_LIST
{
    WSD_URI_LIST* Next;
    const WCHAR* Element;
};

// 
// Structure definition WSD_SCOPES
// 
struct _WSD_SCOPES
{
    const WCHAR* MatchBy;
    WSD_URI_LIST* Scopes;
};

// 
// Structure definition WSD_NAME_LIST
// 
struct _WSD_NAME_LIST
{
    WSD_NAME_LIST* Next;
    WSDXML_NAME* Element;
};

// 
// Structure definition WSD_HELLO
// 
struct _WSD_HELLO
{
    WSD_ENDPOINT_REFERENCE* EndpointReference;
    WSD_NAME_LIST* Types;
    WSD_SCOPES* Scopes;
    WSD_URI_LIST* XAddrs;
    ULONGLONG MetadataVersion;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_REFERENCE_PARAMETERS
// 
struct _WSD_REFERENCE_PARAMETERS
{
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_REFERENCE_PROPERTIES
// 
struct _WSD_REFERENCE_PROPERTIES
{
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_ENDPOINT_REFERENCE
// 
struct _WSD_ENDPOINT_REFERENCE
{
    const WCHAR* Address;
    WSD_REFERENCE_PROPERTIES ReferenceProperties;
    WSD_REFERENCE_PARAMETERS ReferenceParameters;
    WSDXML_NAME* PortType;
    WSDXML_NAME* ServiceName;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_METADATA_SECTION
// 
struct _WSD_METADATA_SECTION
{
    const WCHAR* Dialect;
    const WCHAR* Identifier;
    void* Data;
    WSD_ENDPOINT_REFERENCE* MetadataReference;
    const WCHAR* Location;
    WSDXML_ELEMENT* Any;
};

// 
// Structure definition WSD_METADATA_SECTION_LIST
// 
struct _WSD_METADATA_SECTION_LIST
{
    WSD_METADATA_SECTION_LIST* Next;
    WSD_METADATA_SECTION* Element;
};

// 
// Structure definition WSD_EVENTING_FILTER
// 
struct _WSD_EVENTING_FILTER
{
    const WCHAR* Dialect;
    void* Data;
};

// 
// Structure definition WSD_EVENTING_EXPIRES
// 
struct _WSD_EVENTING_EXPIRES
{
    WSD_DURATION* Duration;
    WSD_DATETIME* DateTime;
};

// 
// Structure definition WSD_EVENTING_DELIVERY_MODE
// 
struct _WSD_EVENTING_DELIVERY_MODE
{
    const WCHAR* Mode;
    void* Data;
};

// 
// Structure definition WSD_LOCALIZED_STRING
// 
struct _WSD_LOCALIZED_STRING
{
    const WCHAR* lang;
    const WCHAR* String;
};

#define TYPE_ENCODING_WSD_RELATIONSHIP_METADATA WSDXML_TYPE_ENCODING(0,0)
extern WSDXML_TYPE Type_WSD_RELATIONSHIP_METADATA;

#define TYPE_ENCODING_WSD_HOST_METADATA WSDXML_TYPE_ENCODING(1,0)
extern WSDXML_TYPE Type_WSD_HOST_METADATA;

#define TYPE_ENCODING_WSD_SERVICE_METADATA WSDXML_TYPE_ENCODING(2,0)
extern WSDXML_TYPE Type_WSD_SERVICE_METADATA;

#define TYPE_ENCODING_WSD_EVENTING_DELIVERY_MODE_PUSH WSDXML_TYPE_ENCODING(3,0)
extern WSDXML_TYPE Type_WSD_EVENTING_DELIVERY_MODE_PUSH;

#define TYPE_ENCODING_WSD_EVENTING_FILTER_ACTION WSDXML_TYPE_ENCODING(4,0)
extern WSDXML_TYPE Type_WSD_EVENTING_FILTER_ACTION;

#define TYPE_ENCODING_WSD_THIS_DEVICE_METADATA WSDXML_TYPE_ENCODING(5,0)
extern WSDXML_TYPE Type_WSD_THIS_DEVICE_METADATA;

#define TYPE_ENCODING_WSD_THIS_MODEL_METADATA WSDXML_TYPE_ENCODING(6,0)
extern WSDXML_TYPE Type_WSD_THIS_MODEL_METADATA;

#define TYPE_ENCODING_WSD_SOAP_FAULT_REASON WSDXML_TYPE_ENCODING(7,0)
extern WSDXML_TYPE Type_WSD_SOAP_FAULT_REASON;

#define TYPE_ENCODING_WSD_SOAP_FAULT_SUBCODE WSDXML_TYPE_ENCODING(8,0)
extern WSDXML_TYPE Type_WSD_SOAP_FAULT_SUBCODE;

#define TYPE_ENCODING_WSD_SOAP_FAULT_CODE WSDXML_TYPE_ENCODING(9,0)
extern WSDXML_TYPE Type_WSD_SOAP_FAULT_CODE;

#define TYPE_ENCODING_WSD_SOAP_FAULT WSDXML_TYPE_ENCODING(10,0)
extern WSDXML_TYPE Type_WSD_SOAP_FAULT;

#define TYPE_ENCODING_WSD_APP_SEQUENCE WSDXML_TYPE_ENCODING(11,0)
extern WSDXML_TYPE Type_WSD_APP_SEQUENCE;

#define TYPE_ENCODING_WSD_HEADER_RELATESTO WSDXML_TYPE_ENCODING(12,0)
extern WSDXML_TYPE Type_WSD_HEADER_RELATESTO;

#define TYPE_ENCODING_WSD_SOAP_HEADER WSDXML_TYPE_ENCODING(13,0)
extern WSDXML_TYPE Type_WSD_SOAP_HEADER;

#define TYPE_ENCODING_WSD_SOAP_MESSAGE WSDXML_TYPE_ENCODING(14,0)
extern WSDXML_TYPE Type_WSD_SOAP_MESSAGE;

#define TYPE_ENCODING_WSD_RESOLVE_MATCHES WSDXML_TYPE_ENCODING(15,0)
extern WSDXML_TYPE Type_WSD_RESOLVE_MATCHES;

#define TYPE_ENCODING_WSD_RESOLVE_MATCH WSDXML_TYPE_ENCODING(16,0)
extern WSDXML_TYPE Type_WSD_RESOLVE_MATCH;

#define TYPE_ENCODING_WSD_RESOLVE WSDXML_TYPE_ENCODING(17,0)
extern WSDXML_TYPE Type_WSD_RESOLVE;

#define TYPE_ENCODING_WSD_PROBE_MATCH WSDXML_TYPE_ENCODING(18,0)
extern WSDXML_TYPE Type_WSD_PROBE_MATCH;

#define TYPE_ENCODING_WSD_PROBE_MATCHES WSDXML_TYPE_ENCODING(19,0)
extern WSDXML_TYPE Type_WSD_PROBE_MATCHES;

#define TYPE_ENCODING_WSD_PROBE WSDXML_TYPE_ENCODING(20,0)
extern WSDXML_TYPE Type_WSD_PROBE;

#define TYPE_ENCODING_WSD_BYE WSDXML_TYPE_ENCODING(21,0)
extern WSDXML_TYPE Type_WSD_BYE;

#define TYPE_ENCODING_WSD_SCOPES WSDXML_TYPE_ENCODING(22,0)
extern WSDXML_TYPE Type_WSD_SCOPES;

#define TYPE_ENCODING_WSD_HELLO WSDXML_TYPE_ENCODING(23,0)
extern WSDXML_TYPE Type_WSD_HELLO;

#define TYPE_ENCODING_WSD_REFERENCE_PARAMETERS WSDXML_TYPE_ENCODING(24,0)
extern WSDXML_TYPE Type_WSD_REFERENCE_PARAMETERS;

#define TYPE_ENCODING_WSD_REFERENCE_PROPERTIES WSDXML_TYPE_ENCODING(25,0)
extern WSDXML_TYPE Type_WSD_REFERENCE_PROPERTIES;

#define TYPE_ENCODING_WSD_ENDPOINT_REFERENCE WSDXML_TYPE_ENCODING(26,0)
extern WSDXML_TYPE Type_WSD_ENDPOINT_REFERENCE;

#define TYPE_ENCODING_WSD_METADATA_SECTION WSDXML_TYPE_ENCODING(27,0)
extern WSDXML_TYPE Type_WSD_METADATA_SECTION;

#define TYPE_ENCODING_WSD_EVENTING_FILTER WSDXML_TYPE_ENCODING(28,0)
extern WSDXML_TYPE Type_WSD_EVENTING_FILTER;

#define TYPE_ENCODING_WSD_EVENTING_EXPIRES WSDXML_TYPE_ENCODING(29,0)
extern WSDXML_TYPE Type_WSD_EVENTING_EXPIRES;

#define TYPE_ENCODING_WSD_EVENTING_DELIVERY_MODE WSDXML_TYPE_ENCODING(30,0)
extern WSDXML_TYPE Type_WSD_EVENTING_DELIVERY_MODE;

#define TYPE_ENCODING_WSD_LOCALIZED_STRING WSDXML_TYPE_ENCODING(31,0)
extern WSDXML_TYPE Type_WSD_LOCALIZED_STRING;


extern WSDXML_TYPE* WSDTypes[32];
#define WSDRegisterTypes(pContext) pContext->SetTypes(WSDTypes,(sizeof(WSDTypes) / sizeof(WSDTypes[0])),0)

//
// Port type http://schemas.xmlsoap.org/ws/2004/09/mex/mex
// Message structure definitions
//
typedef struct
{
    WSD_METADATA_SECTION_LIST* Metadata;
}
RESPONSEBODY_GetMetadata;

//
// Port type http://schemas.xmlsoap.org/ws/2004/08/eventing/Eventing
// Message structure definitions
//
typedef struct
{
    WSD_ENDPOINT_REFERENCE* EndTo;
    WSD_EVENTING_DELIVERY_MODE* Delivery;
    WSD_EVENTING_EXPIRES* Expires;
    WSD_EVENTING_FILTER* Filter;
    WSDXML_ELEMENT* Any;
}
REQUESTBODY_Subscribe;

typedef struct
{
    WSD_ENDPOINT_REFERENCE* SubscriptionManager;
    WSD_EVENTING_EXPIRES* expires;
    WSDXML_ELEMENT* any;
}
RESPONSEBODY_Subscribe;

typedef struct
{
    WSD_EVENTING_EXPIRES* Expires;
    WSDXML_ELEMENT* Any;
}
REQUESTBODY_Renew;

typedef struct
{
    WSD_EVENTING_EXPIRES* expires;
    WSDXML_ELEMENT* any;
}
RESPONSEBODY_Renew;

typedef struct
{
    WSDXML_ELEMENT* Any;
}
REQUESTBODY_GetStatus;

typedef struct
{
    WSD_EVENTING_EXPIRES* expires;
    WSDXML_ELEMENT* any;
}
RESPONSEBODY_GetStatus;

typedef struct
{
    WSDXML_ELEMENT* any;
}
REQUESTBODY_Unsubscribe;

//
// Port type http://schemas.xmlsoap.org/ws/2004/08/eventing/EventSink
// Message structure definitions
//
typedef struct
{
    WSD_ENDPOINT_REFERENCE* SubscriptionManager;
    const WCHAR* Status;
    WSD_LOCALIZED_STRING* Reason;
    WSDXML_ELEMENT* Any;
}
RESPONSEBODY_SubscriptionEnd;

 

typedef struct _WSD_UNKNOWN_LOOKUP
{
    WSDXML_ELEMENT* Any;
} WSD_UNKNOWN_LOOKUP;

struct _WSD_EVENT
{
    HRESULT Hr;
    DWORD EventType;
    WCHAR* DispatchTag;
    WSD_HANDLER_CONTEXT HandlerContext;
    WSD_SOAP_MESSAGE* Soap;
    WSD_OPERATION* Operation;
    IWSDMessageParameters* MessageParameters;
};

        

