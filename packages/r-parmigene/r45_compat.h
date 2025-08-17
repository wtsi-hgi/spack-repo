#ifndef R_PARMIGENE_R45_COMPAT_H
#define R_PARMIGENE_R45_COMPAT_H
#include <R.h>
#include <R_ext/RS.h>
#include <R_ext/Memory.h>
#ifndef Calloc
#define Calloc(n, T) (T*) R_Calloc((n), T)
#endif
#ifndef Realloc
#define Realloc(p, n, T) (T*) R_Realloc((p), (n), T)
#endif
#ifndef Free
#define Free(p) R_Free(p)
#endif
#endif /* R_PARMIGENE_R45_COMPAT_H */
