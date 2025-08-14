from spack.package import *


class RFf(RPackage):
    """
    Memory-Efficient Storage of Large Data on Disk and Fast Access Functions.
    """

    homepage = "https://cloud.r-project.org/package=ff"
    cran = "ff"

    version("4.0.12", sha256="08af355a9a10fe29d48d085abc7cf1f975e1a4a670668a4f8d9632d087fb41bf")
    version("4.0.9", sha256="8f4341b81b19842b23f3cee464ca7d3e0efbb0b1368d02c7b94af9fe171b2f0e")
    version("4.0.7", sha256="7a7e921b29f87f1f8a3a4b931d7d54bd9eb52f2b24585d4e3b9cb2dbf78c33d1")

    depends_on("r@2.13:")
    depends_on("r-bit", type=("build", "run"))

    def patch(self):
        # Inline source edit to restore Calloc/Free compatibility for R >= 4.5
        insertion = (
            "#include <Rinternals.h>\n"
            "#include <R_ext/Memory.h>\n"
            "#include <stddef.h>\n"
            "#ifndef Calloc\n"
            "#define Calloc(b, T) (T*) R_chk_calloc((size_t)(b), sizeof(T))\n"
            "#endif\n"
            "#ifndef Free\n"
            "#define Free(p) R_chk_free((void*)(p))\n"
            "#endif\n"
        )
        filter_file(r"#include <Rinternals.h>", insertion, "src/ordermerge.c")
