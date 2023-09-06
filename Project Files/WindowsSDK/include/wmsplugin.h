

/* this ALWAYS GENERATED file contains the definitions for the interfaces */


 /* File created by MIDL compiler version 7.00.0499 */
/* Compiler settings for wmsplugin.idl:
    Oicf, W1, Zp8, env=Win32 (32b run)
    protocol : dce , ms_ext, c_ext, robust
    error checks: allocation ref bounds_check enum stub_data 
    VC __declspec() decoration level: 
         __declspec(uuid()), __declspec(selectany), __declspec(novtable)
         DECLSPEC_UUID(), MIDL_INTERFACE()
*/
//@@MIDL_FILE_HEADING(  )

#pragma warning( disable: 4049 )  /* more than 64k source lines */


/* verify that the <rpcndr.h> version is high enough to compile this file*/
#ifndef __REQUIRED_RPCNDR_H_VERSION__
#define __REQUIRED_RPCNDR_H_VERSION__ 500
#endif

/* verify that the <rpcsal.h> version is high enough to compile this file*/
#ifndef __REQUIRED_RPCSAL_H_VERSION__
#define __REQUIRED_RPCSAL_H_VERSION__ 100
#endif

#include "rpc.h"
#include "rpcndr.h"

#ifndef __RPCNDR_H_VERSION__
#error this stub requires an updated version of <rpcndr.h>
#endif // __RPCNDR_H_VERSION__

#ifndef COM_NO_WINDOWS_H
#include "windows.h"
#include "ole2.h"
#endif /*COM_NO_WINDOWS_H*/

#ifndef __wmsplugin_h__
#define __wmsplugin_h__

#if defined(_MSC_VER) && (_MSC_VER >= 1020)
#pragma once
#endif

/* Forward Declarations */ 

#ifndef __IWMSPlugin_FWD_DEFINED__
#define __IWMSPlugin_FWD_DEFINED__
typedef interface IWMSPlugin IWMSPlugin;
#endif 	/* __IWMSPlugin_FWD_DEFINED__ */


/* header files for imported files */
#include "oaidl.h"
#include "WMSNamedValues.h"

#ifdef __cplusplus
extern "C"{
#endif 


/* interface __MIDL_itf_wmsplugin_0000_0000 */
/* [local] */ 

//*****************************************************************************
//
// Microsoft Windows Media
// Copyright (C) Microsoft Corporation. All rights reserved.
//
// Automatically generated by Midl from wmsplugin.idl
//
// DO NOT EDIT THIS FILE.
//
//*****************************************************************************
typedef /* [uuid][public] */  DECLSPEC_UUID("56209C38-39FA-432a-8068-307B7BAE01B8") 
enum WMS_PLUGIN_LOAD_TYPE
    {	WMS_PLUGIN_LOAD_TYPE_UNSPECIFIED	= 0,
	WMS_PLUGIN_LOAD_TYPE_IN_PROC	= 1,
	WMS_PLUGIN_LOAD_TYPE_OUT_OF_PROC	= 2,
	WMS_NUM_PLUGIN_LOAD_TYPE	= 3
    } 	WMS_PLUGIN_LOAD_TYPE;

typedef /* [uuid][public] */  DECLSPEC_UUID("56209C39-39FA-432a-8068-307B7BAE01B8") 
enum WMS_PLUGIN_UNSUPPORTED_LOAD_TYPE
    {	WMS_PLUGIN_UNSUPPORTED_LOAD_TYPE_NONE	= 0,
	WMS_PLUGIN_UNSUPPORTED_LOAD_TYPE_IN_PROC	= 1,
	WMS_PLUGIN_UNSUPPORTED_LOAD_TYPE_OUT_OF_PROC	= 2
    } 	WMS_PLUGIN_UNSUPPORTED_LOAD_TYPE;

typedef /* [uuid][public] */  DECLSPEC_UUID("8AC2B32C-A223-4134-8DCF-6673C95CE924") 
enum WMS_PLUGIN_SUPPORT_TYPE
    {	WMS_PLUGIN_SUPPORT_IS_SUPPORTED	= 0,
	WMS_PLUGIN_SUPPORT_REQUIRES_ADVANCED_SERVER	= 1
    } 	WMS_PLUGIN_SUPPORT_TYPE;



extern RPC_IF_HANDLE __MIDL_itf_wmsplugin_0000_0000_v0_0_c_ifspec;
extern RPC_IF_HANDLE __MIDL_itf_wmsplugin_0000_0000_v0_0_s_ifspec;

#ifndef __IWMSPlugin_INTERFACE_DEFINED__
#define __IWMSPlugin_INTERFACE_DEFINED__

/* interface IWMSPlugin */
/* [unique][helpstring][nonextensible][dual][uuid][object] */ 

typedef /* [uuid][public] */  DECLSPEC_UUID("3E52E0E2-72A7-11D2-BF2F-00805FBE84A6") 
enum WMS_PLUGIN_STATUS
    {	WMS_PLUGIN_NONE	= 0,
	WMS_PLUGIN_ERROR	= 0x1,
	WMS_PLUGIN_LOADED	= 0x2,
	WMS_PLUGIN_ENABLED	= 0x4,
	WMS_PLUGIN_LOADED_IN_PROC	= 0x8,
	WMS_PLUGIN_LOADED_OUT_OF_PROC	= 0x10,
	WMS_PLUGIN_REMOVE_ON_SERVICE_RESTART	= 0x20
    } 	WMS_PLUGIN_STATUS;


EXTERN_C const IID IID_IWMSPlugin;

#if defined(__cplusplus) && !defined(CINTERFACE)
    
    MIDL_INTERFACE("517758ed-603c-4b98-82c1-4b2fa7787166")
    IWMSPlugin : public IDispatch
    {
    public:
        virtual /* [helpstring][id][propput] */ HRESULT STDMETHODCALLTYPE put_Name( 
            /* [in] */ __RPC__in BSTR pVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_Name( 
            /* [retval][out] */ __RPC__deref_out_opt BSTR *pVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_Enabled( 
            /* [retval][out] */ __RPC__out VARIANT_BOOL *pVal) = 0;
        
        virtual /* [helpstring][id][propput] */ HRESULT STDMETHODCALLTYPE put_Enabled( 
            /* [in] */ VARIANT_BOOL newVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_CLSID( 
            /* [retval][out] */ __RPC__deref_out_opt BSTR *pVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_CustomInterface( 
            /* [retval][out] */ __RPC__deref_out_opt IDispatch **ppVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_Status( 
            /* [retval][out] */ __RPC__out long *pVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_ErrorCode( 
            /* [retval][out] */ __RPC__out long *pVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_Properties( 
            /* [retval][out] */ __RPC__deref_out_opt IWMSNamedValues **pVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_Version( 
            /* [retval][out] */ __RPC__deref_out_opt BSTR *pVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_LoadType( 
            /* [retval][out] */ __RPC__out WMS_PLUGIN_LOAD_TYPE *pVal) = 0;
        
        virtual /* [helpstring][id][propput] */ HRESULT STDMETHODCALLTYPE put_LoadType( 
            /* [in] */ WMS_PLUGIN_LOAD_TYPE val) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_ErrorText( 
            /* [retval][out] */ __RPC__deref_out_opt BSTR *pVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_SelectionOrder( 
            /* [retval][out] */ __RPC__out long *pVal) = 0;
        
        virtual /* [helpstring][id][propput] */ HRESULT STDMETHODCALLTYPE put_SelectionOrder( 
            /* [in] */ long lVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_SupportStatus( 
            /* [retval][out] */ __RPC__out WMS_PLUGIN_SUPPORT_TYPE *pVal) = 0;
        
        virtual /* [helpstring][id][propget] */ HRESULT STDMETHODCALLTYPE get_MonikerName( 
            /* [retval][out] */ __RPC__deref_out_opt BSTR *pbstrVal) = 0;
        
    };
    
#else 	/* C style interface */

    typedef struct IWMSPluginVtbl
    {
        BEGIN_INTERFACE
        
        HRESULT ( STDMETHODCALLTYPE *QueryInterface )( 
            IWMSPlugin * This,
            /* [in] */ __RPC__in REFIID riid,
            /* [iid_is][out] */ 
            __RPC__deref_out  void **ppvObject);
        
        ULONG ( STDMETHODCALLTYPE *AddRef )( 
            IWMSPlugin * This);
        
        ULONG ( STDMETHODCALLTYPE *Release )( 
            IWMSPlugin * This);
        
        HRESULT ( STDMETHODCALLTYPE *GetTypeInfoCount )( 
            IWMSPlugin * This,
            /* [out] */ __RPC__out UINT *pctinfo);
        
        HRESULT ( STDMETHODCALLTYPE *GetTypeInfo )( 
            IWMSPlugin * This,
            /* [in] */ UINT iTInfo,
            /* [in] */ LCID lcid,
            /* [out] */ __RPC__deref_out_opt ITypeInfo **ppTInfo);
        
        HRESULT ( STDMETHODCALLTYPE *GetIDsOfNames )( 
            IWMSPlugin * This,
            /* [in] */ __RPC__in REFIID riid,
            /* [size_is][in] */ __RPC__in_ecount_full(cNames) LPOLESTR *rgszNames,
            /* [range][in] */ UINT cNames,
            /* [in] */ LCID lcid,
            /* [size_is][out] */ __RPC__out_ecount_full(cNames) DISPID *rgDispId);
        
        /* [local] */ HRESULT ( STDMETHODCALLTYPE *Invoke )( 
            IWMSPlugin * This,
            /* [in] */ DISPID dispIdMember,
            /* [in] */ REFIID riid,
            /* [in] */ LCID lcid,
            /* [in] */ WORD wFlags,
            /* [out][in] */ DISPPARAMS *pDispParams,
            /* [out] */ VARIANT *pVarResult,
            /* [out] */ EXCEPINFO *pExcepInfo,
            /* [out] */ UINT *puArgErr);
        
        /* [helpstring][id][propput] */ HRESULT ( STDMETHODCALLTYPE *put_Name )( 
            IWMSPlugin * This,
            /* [in] */ __RPC__in BSTR pVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_Name )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__deref_out_opt BSTR *pVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_Enabled )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__out VARIANT_BOOL *pVal);
        
        /* [helpstring][id][propput] */ HRESULT ( STDMETHODCALLTYPE *put_Enabled )( 
            IWMSPlugin * This,
            /* [in] */ VARIANT_BOOL newVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_CLSID )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__deref_out_opt BSTR *pVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_CustomInterface )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__deref_out_opt IDispatch **ppVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_Status )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__out long *pVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_ErrorCode )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__out long *pVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_Properties )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__deref_out_opt IWMSNamedValues **pVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_Version )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__deref_out_opt BSTR *pVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_LoadType )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__out WMS_PLUGIN_LOAD_TYPE *pVal);
        
        /* [helpstring][id][propput] */ HRESULT ( STDMETHODCALLTYPE *put_LoadType )( 
            IWMSPlugin * This,
            /* [in] */ WMS_PLUGIN_LOAD_TYPE val);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_ErrorText )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__deref_out_opt BSTR *pVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_SelectionOrder )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__out long *pVal);
        
        /* [helpstring][id][propput] */ HRESULT ( STDMETHODCALLTYPE *put_SelectionOrder )( 
            IWMSPlugin * This,
            /* [in] */ long lVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_SupportStatus )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__out WMS_PLUGIN_SUPPORT_TYPE *pVal);
        
        /* [helpstring][id][propget] */ HRESULT ( STDMETHODCALLTYPE *get_MonikerName )( 
            IWMSPlugin * This,
            /* [retval][out] */ __RPC__deref_out_opt BSTR *pbstrVal);
        
        END_INTERFACE
    } IWMSPluginVtbl;

    interface IWMSPlugin
    {
        CONST_VTBL struct IWMSPluginVtbl *lpVtbl;
    };

    

#ifdef COBJMACROS


#define IWMSPlugin_QueryInterface(This,riid,ppvObject)	\
    ( (This)->lpVtbl -> QueryInterface(This,riid,ppvObject) ) 

#define IWMSPlugin_AddRef(This)	\
    ( (This)->lpVtbl -> AddRef(This) ) 

#define IWMSPlugin_Release(This)	\
    ( (This)->lpVtbl -> Release(This) ) 


#define IWMSPlugin_GetTypeInfoCount(This,pctinfo)	\
    ( (This)->lpVtbl -> GetTypeInfoCount(This,pctinfo) ) 

#define IWMSPlugin_GetTypeInfo(This,iTInfo,lcid,ppTInfo)	\
    ( (This)->lpVtbl -> GetTypeInfo(This,iTInfo,lcid,ppTInfo) ) 

#define IWMSPlugin_GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId)	\
    ( (This)->lpVtbl -> GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId) ) 

#define IWMSPlugin_Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr)	\
    ( (This)->lpVtbl -> Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr) ) 


#define IWMSPlugin_put_Name(This,pVal)	\
    ( (This)->lpVtbl -> put_Name(This,pVal) ) 

#define IWMSPlugin_get_Name(This,pVal)	\
    ( (This)->lpVtbl -> get_Name(This,pVal) ) 

#define IWMSPlugin_get_Enabled(This,pVal)	\
    ( (This)->lpVtbl -> get_Enabled(This,pVal) ) 

#define IWMSPlugin_put_Enabled(This,newVal)	\
    ( (This)->lpVtbl -> put_Enabled(This,newVal) ) 

#define IWMSPlugin_get_CLSID(This,pVal)	\
    ( (This)->lpVtbl -> get_CLSID(This,pVal) ) 

#define IWMSPlugin_get_CustomInterface(This,ppVal)	\
    ( (This)->lpVtbl -> get_CustomInterface(This,ppVal) ) 

#define IWMSPlugin_get_Status(This,pVal)	\
    ( (This)->lpVtbl -> get_Status(This,pVal) ) 

#define IWMSPlugin_get_ErrorCode(This,pVal)	\
    ( (This)->lpVtbl -> get_ErrorCode(This,pVal) ) 

#define IWMSPlugin_get_Properties(This,pVal)	\
    ( (This)->lpVtbl -> get_Properties(This,pVal) ) 

#define IWMSPlugin_get_Version(This,pVal)	\
    ( (This)->lpVtbl -> get_Version(This,pVal) ) 

#define IWMSPlugin_get_LoadType(This,pVal)	\
    ( (This)->lpVtbl -> get_LoadType(This,pVal) ) 

#define IWMSPlugin_put_LoadType(This,val)	\
    ( (This)->lpVtbl -> put_LoadType(This,val) ) 

#define IWMSPlugin_get_ErrorText(This,pVal)	\
    ( (This)->lpVtbl -> get_ErrorText(This,pVal) ) 

#define IWMSPlugin_get_SelectionOrder(This,pVal)	\
    ( (This)->lpVtbl -> get_SelectionOrder(This,pVal) ) 

#define IWMSPlugin_put_SelectionOrder(This,lVal)	\
    ( (This)->lpVtbl -> put_SelectionOrder(This,lVal) ) 

#define IWMSPlugin_get_SupportStatus(This,pVal)	\
    ( (This)->lpVtbl -> get_SupportStatus(This,pVal) ) 

#define IWMSPlugin_get_MonikerName(This,pbstrVal)	\
    ( (This)->lpVtbl -> get_MonikerName(This,pbstrVal) ) 

#endif /* COBJMACROS */


#endif 	/* C style interface */




#endif 	/* __IWMSPlugin_INTERFACE_DEFINED__ */


/* Additional Prototypes for ALL interfaces */

unsigned long             __RPC_USER  BSTR_UserSize(     unsigned long *, unsigned long            , BSTR * ); 
unsigned char * __RPC_USER  BSTR_UserMarshal(  unsigned long *, unsigned char *, BSTR * ); 
unsigned char * __RPC_USER  BSTR_UserUnmarshal(unsigned long *, unsigned char *, BSTR * ); 
void                      __RPC_USER  BSTR_UserFree(     unsigned long *, BSTR * ); 

unsigned long             __RPC_USER  BSTR_UserSize64(     unsigned long *, unsigned long            , BSTR * ); 
unsigned char * __RPC_USER  BSTR_UserMarshal64(  unsigned long *, unsigned char *, BSTR * ); 
unsigned char * __RPC_USER  BSTR_UserUnmarshal64(unsigned long *, unsigned char *, BSTR * ); 
void                      __RPC_USER  BSTR_UserFree64(     unsigned long *, BSTR * ); 

/* end of Additional Prototypes */

#ifdef __cplusplus
}
#endif

#endif



