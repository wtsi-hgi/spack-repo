from spack.package import *


class RCatools(RPackage):
    """Moving Window Statistics, GIF, Base64, ROC AUC, etc."""

    cran = "caTools"

    version("1.18.2", sha256="75d61115afec754b053ed1732cc034f2aeb27b13e6e1932aa0f26bf590cf0293")
    version("1.18.1", sha256="ffeba4ffbeed5d491bf79b1fde3477f413341e412f77316af20439f54447c9f9")
    version("1.17.1.2", sha256="69cc542fab5677462b1a768709d0c4a0a0790f5db53e1fe9ae7123787c18726b")
    version("1.17.1.1", sha256="d53e2c5c77f1bd4744703d7196dbc9b4671a120bbb5b9b3edc45fc57c0650c06")
    version("1.17.1", sha256="d32a73febf00930355cc00f3e4e71357412e0f163faae6a4bf7f552cacfe9af4")

    depends_on("r", type=("build", "run"))
    depends_on("r-bitops", type=("build", "run"))

    # Fix build with R >= 4.5 where Calloc/Free macros were removed
    # Apply inline source edits instead of external patch to be robust to CRAN layout
    def patch(self):
        # Add R_ext/Memory.h and map deprecated Calloc/Free to R_Calloc/R_Free
        filter_file(
            r"#include <Rinternals.h>",
            (
                "#include <Rinternals.h>\n"
                "#include <R_ext/Memory.h>\n"
                "#ifndef Calloc\n"
                "#define Calloc(b, t)  (t*) R_Calloc((b), t)\n"
                "#endif\n"
                "#ifndef Free\n"
                "#define Free R_Free\n"
                "#endif\n"
            ),
            "src/runfunc.c",
        )

        filter_file(
            r"#include <Rinternals.h>",
            (
                "#include <Rinternals.h>\n"
                "#include <R_ext/Memory.h>\n"
                "#ifndef Calloc\n"
                "#define Calloc(b, T) (T*) R_Calloc((b), T)\n"
                "#endif\n"
                "#ifndef Free\n"
                "#define Free R_Free\n"
                "#endif\n"
            ),
            "src/GifTools.h",
        )
