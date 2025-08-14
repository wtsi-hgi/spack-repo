#ifndef R_FDRTOOL_R45_COMPAT_H
#define R_FDRTOOL_R45_COMPAT_H

#include <stdlib.h>
#include <stddef.h>

#ifndef Calloc
#define Calloc(n, t) ((t*) calloc((size_t)(n), sizeof(t)))
#endif

#ifndef Free
#define Free(p) free(p)
#endif

#endif /* R_FDRTOOL_R45_COMPAT_H */
