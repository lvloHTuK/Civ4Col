

/* this ALWAYS GENERATED file contains the definitions for the interfaces */


 /* File created by MIDL compiler version 7.00.0499 */
/* Compiler settings for iisrsta.idl:
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

#ifndef __iisrsta_h__
#define __iisrsta_h__

#if defined(_MSC_VER) && (_MSC_VER >= 1020)
#pragma once
#endif

/* Forward Declarations */ 

#ifndef __IIisServiceControl_FWD_DEFINED__
#define __IIisServiceControl_FWD_DEFINED__
typedef interface IIisServiceControl IIisServiceControl;
#endif 	/* __IIisServiceControl_FWD_DEFINED__ */


#ifndef __IisServiceControl_FWD_DEFINED__
#define __IisServiceControl_FWD_DEFINED__

#ifdef __cplusplus
typedef class IisServiceControl IisServiceControl;
#else
typedef struct IisServiceControl IisServiceControl;
#endif /* __cplusplus */

#endif 	/* __IisServiceControl_FWD_DEFINED__ */


/* header files for imported files */
#include "oaidl.h"
#include "ocidl.h"

#ifdef __cplusplus
extern "C"{
#endif 


/* interface __MIDL_itf_iisrsta_0000_0000 */
/* [local] */ 

DEFINE_GUID(IID_IIisServiceControl, 0xE8FB8620, 0x588F, 0x11d2, 0x9d, 0x61, 0x0,0xc0, 0x4f, 0x79, 0xc5, 0xfe);
DEFINE_GUID(CLSID_IisServiceControl, 0xE8FB8621, 0x588F, 0x11d2, 0x9d, 0x61, 0x0,0xc0, 0x4f, 0x79, 0xc5, 0xfe);
DEFINE_GUID(LIBID_IISRSTALib, 0xE8FB8614, 0x588F, 0x11d2, 0x9d, 0x61, 0x0,0xc0, 0x4f, 0x79, 0xc5, 0xfe);


extern RPC_IF_HANDLE __MIDL_itf_iisrsta_0000_0000_v0_0_c_ifspec;
extern RPC_IF_HANDLE __MIDL_itf_iisrsta_0000_0000_v0_0_s_ifspec;

#ifndef __IIisServiceControl_INTERFACE_DEFINED__
#define __IIisServiceControl_INTERFACE_DEFINED__

/* interface IIisServiceControl */
/* [unique][helpstring][dual][uuid][object] */ 


EXTERN_C const IID IID_IIisServiceControl;

#if defined(__cplusplus) && !defined(CINTERFACE)
    
    MIDL_INTERFACE("E8FB8620-588F-11D2-9D61-00C04F79C5FE")
    IIisServiceControl : public IDispatch
    {
    public:
        virtual /* [helpstring][id] */ HRESULT STDMETHODCALLTYPE Stop( 
            DWORD dwTimeoutMsecs,
            DWORD dwForce) = 0;
        
        virtual /* [helpstring][id] */ HRESULT STDMETHODCALLTYPE Start( 
            DWORD dwTimeoutMsecs) = 0;
        
        virtual /* [helpstring][id] */ HRESULT STDMETHODCALLTYPE Reboot( 
            DWORD dwTimeouMsecs,
            DWORD dwForceAppsClosed) = 0;
        
        virtual /* [helpstring][id] */ HRESULT STDMETHODCALLTYPE Status( 
            /* [in] */ DWORD dwBufferSize,
            /* [size_is][out] */ __RPC__out_ecount_full(dwBufferSize) unsigned char *pbBuffer,
            /* [out] */ __RPC__out DWORD *pdwMDRequiredBufferSize,
            /* [out] */ __RPC__out DWORD *pdwNumServices) = 0;
        
        virtual /* [helpstring][id] */ HRESULT STDMETHODCALLTYPE Kill( void) = 0;
        
    };
    
#else 	/* C style interface */

    typedef struct IIisServiceControlVtbl
    {
        BEGIN_INTERFACE
        
        HRESULT ( STDMETHODCALLTYPE *QueryInterface )( 
            IIisServiceControl * This,
            /* [in] */ __RPC__in REFIID riid,
            /* [iid_is][out] */ 
            __RPC__deref_out  void **ppvObject);
        
        ULONG ( STDMETHODCALLTYPE *AddRef )( 
            IIisServiceControl * This);
        
        ULONG ( STDMETHODCALLTYPE *Release )( 
            IIisServiceControl * This);
        
        HRESULT ( STDMETHODCALLTYPE *GetTypeInfoCount )( 
            IIisServiceControl * This,
            /* [out] */ __RPC__out UINT *pctinfo);
        
        HRESULT ( STDMETHODCALLTYPE *GetTypeInfo )( 
            IIisServiceControl * This,
            /* [in] */ UINT iTInfo,
            /* [in] */ LCID lcid,
            /* [out] */ __RPC__deref_out_opt ITypeInfo **ppTInfo);
        
        HRESULT ( STDMETHODCALLTYPE *GetIDsOfNames )( 
            IIisServiceControl * This,
            /* [in] */ __RPC__in REFIID riid,
            /* [size_is][in] */ __RPC__in_ecount_full(cNames) LPOLESTR *rgszNames,
            /* [range][in] */ UINT cNames,
            /* [in] */ LCID lcid,
            /* [size_is][out] */ __RPC__out_ecount_full(cNames) DISPID *rgDispId);
        
        /* [local] */ HRESULT ( STDMETHODCALLTYPE *Invoke )( 
            IIisServiceControl * This,
            /* [in] */ DISPID dispIdMember,
            /* [in] */ REFIID riid,
            /* [in] */ LCID lcid,
            /* [in] */ WORD wFlags,
            /* [out][in] */ DISPPARAMS *pDispParams,
            /* [out] */ VARIANT *pVarResult,
            /* [out] */ EXCEPINFO *pExcepInfo,
            /* [out] */ UINT *puArgErr);
        
        /* [helpstring][id] */ HRESULT ( STDMETHODCALLTYPE *Stop )( 
            IIisServiceControl * This,
            DWORD dwTimeoutMsecs,
            DWORD dwForce);
        
        /* [helpstring][id] */ HRESULT ( STDMETHODCALLTYPE *Start )( 
            IIisServiceControl * This,
            DWORD dwTimeoutMsecs);
        
        /* [helpstring][id] */ HRESULT ( STDMETHODCALLTYPE *Reboot )( 
            IIisServiceControl * This,
            DWORD dwTimeouMsecs,
            DWORD dwForceAppsClosed);
        
        /* [helpstring][id] */ HRESULT ( STDMETHODCALLTYPE *Status )( 
            IIisServiceControl * This,
            /* [in] */ DWORD dwBufferSize,
            /* [size_is][out] */ __RPC__out_ecount_full(dwBufferSize) unsigned char *pbBuffer,
            /* [out] */ __RPC__out DWORD *pdwMDRequiredBufferSize,
            /* [out] */ __RPC__out DWORD *pdwNumServices);
        
        /* [helpstring][id] */ HRESULT ( STDMETHODCALLTYPE *Kill )( 
            IIisServiceControl * This);
        
        END_INTERFACE
    } IIisServiceControlVtbl;

    interface IIisServiceControl
    {
        CONST_VTBL struct IIisServiceControlVtbl *lpVtbl;
    };

    

#ifdef COBJMACROS


#define IIisServiceControl_QueryInterface(This,riid,ppvObject)	\
    ( (This)->lpVtbl -> QueryInterface(This,riid,ppvObject) ) 

#define IIisServiceControl_AddRef(This)	\
    ( (This)->lpVtbl -> AddRef(This) ) 

#define IIisServiceControl_Release(This)	\
    ( (This)->lpVtbl -> Release(This) ) 


#define IIisServiceControl_GetTypeInfoCount(This,pctinfo)	\
    ( (This)->lpVtbl -> GetTypeInfoCount(This,pctinfo) ) 

#define IIisServiceControl_GetTypeInfo(This,iTInfo,lcid,ppTInfo)	\
    ( (This)->lpVtbl -> GetTypeInfo(This,iTInfo,lcid,ppTInfo) ) 

#define IIisServiceControl_GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId)	\
    ( (This)->lpVtbl -> GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId) ) 

#define IIisServiceControl_Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr)	\
    ( (This)->lpVtbl -> Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr) ) 


#define IIisServiceControl_Stop(This,dwTimeoutMsecs,dwForce)	\
    ( (This)->lpVtbl -> Stop(This,dwTimeoutMsecs,dwForce) ) 

#define IIisServiceControl_Start(This,dwTimeoutMsecs)	\
    ( (This)->lpVtbl -> Start(This,dwTimeoutMsecs) ) 

#define IIisServiceControl_Reboot(This,dwTimeouMsecs,dwForceAppsClosed)	\
    ( (This)->lpVtbl -> Reboot(This,dwTimeouMsecs,dwForceAppsClosed) ) 

#define IIisServiceControl_Status(This,dwBufferSize,pbBuffer,pdwMDRequiredBufferSize,pdwNumServices)	\
    ( (This)->lpVtbl -> Status(This,dwBufferSize,pbBuffer,pdwMDRequiredBufferSize,pdwNumServices) ) 

#define IIisServiceControl_Kill(This)	\
    ( (This)->lpVtbl -> Kill(This) ) 

#endif /* COBJMACROS */


#endif 	/* C style interface */




#endif 	/* __IIisServiceControl_INTERFACE_DEFINED__ */



#ifndef __IISRSTALib_LIBRARY_DEFINED__
#define __IISRSTALib_LIBRARY_DEFINED__

/* library IISRSTALib */
/* [helpstring][version][uuid] */ 


EXTERN_C const IID LIBID_IISRSTALib;

EXTERN_C const CLSID CLSID_IisServiceControl;

#ifdef __cplusplus

class DECLSPEC_UUID("E8FB8621-588F-11D2-9D61-00C04F79C5FE")
IisServiceControl;
#endif
#endif /* __IISRSTALib_LIBRARY_DEFINED__ */

/* interface __MIDL_itf_iisrsta_0000_0001 */
/* [local] */ 

typedef struct {
DWORD iServiceName;
DWORD iDisplayName;
SERVICE_STATUS ServiceStatus;
} SERIALIZED_ENUM_SERVICE_STATUS;


extern RPC_IF_HANDLE __MIDL_itf_iisrsta_0000_0001_v0_0_c_ifspec;
extern RPC_IF_HANDLE __MIDL_itf_iisrsta_0000_0001_v0_0_s_ifspec;

/* Additional Prototypes for ALL interfaces */

/* end of Additional Prototypes */

#ifdef __cplusplus
}
#endif

#endif



