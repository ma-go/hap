////////////////////////////////////////////////////////////////////////////////
// Projekt:              Home-Automation                                      //
// Modul:                Switch                                               //
// Version:              2.1 (0)                                              //
////////////////////////////////////////////////////////////////////////////////
// Erstellt am:          20.12.2005                                           //
// Erstellt von:         Holger Heuser                                        //
// Zuletzt ge�ndert am:  21.01.2006                                           //
// Zuletzt ge�ndert von: Holger Heuser                                        //
////////////////////////////////////////////////////////////////////////////////

#ifndef HASW
#define HASW


////////////////////////////////////////////////////////////////////////////////
// Module einbinden                                                           //
////////////////////////////////////////////////////////////////////////////////

#include <hagl.h>


////////////////////////////////////////////////////////////////////////////////
// Deklarationen                                                              //
////////////////////////////////////////////////////////////////////////////////

void SWInit(void);
inline tByte SWGetValue(tByte pX);
void SWSetValue(tByte pX, tByte pValue);
inline void SWDestroy(void);


#endif
