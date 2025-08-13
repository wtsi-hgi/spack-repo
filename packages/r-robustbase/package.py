# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustbase(RPackage):
    """Basic Robust Statistics.

    "Essential" Robust Statistics. Tools allowing to analyze data with robust
    methods. This includes regression methodology including model selections
    and multivariate statistics where we strive to cover the book "Robust
    Statistics, Theory and Methods" by 'Maronna, Martin and Yohai'; Wiley
    2006."""

    cran = "robustbase"
    version("0.99-2", md5="1b79921bca8334ef03f67f0ca0afd63f")
    version("0.95-1", sha256="862cd26db3ecdf34ab47c52d355fd65ffebbff448aea17999a9b95a1f13ba3ea")
    version("0.95-0", sha256="5cfaea1c46df6d45086614fea5f152c8da8ebfcadf33bb8df5b82e742eef9724")
    version("0.93-9", sha256="d75fb5075463fec61d063bced7003936e9198492328b6fae15f67e8415713c45")
    version("0.93-7", sha256="8911d2d0fdca5e2627033e046279f9d106e25ce98d588f9ccc4d8e4b42680956")
    version("0.93-5", sha256="bde564dbd52f04ab32f9f2f9dd09b9578f3ccd2541cf5f8ff430da42a55e7f56")
    version("0.93-4", sha256="ea9e03d484ef52ea805803477ffc48881e4c8c86ffda4eea56109f8b23f0a6e0")
    version("0.92-7", sha256="fcbd6ccbb0291b599fe6a674a91344511e0a691b9cadba0a9d40037faa22bf8f")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-deoptimr", type=("build", "run"))

    # Add compatibility macros for R >= 4.5 where Calloc/Free macros
    # were removed from legacy headers. Inject lightweight shims.
    def patch(self):
        insertion = (
            "#include <R_ext/RS.h>\n"
            "#ifndef Calloc\n"
            "#define Calloc(n, t) R_Calloc(n, t)\n"
            "#endif\n"
            "#ifndef Realloc\n"
            "#define Realloc(p, n, t) R_Realloc(p, n, t)\n"
            "#endif\n"
            "#ifndef Free\n"
            "#define Free(p) R_Free(p)\n"
            "#endif\n"
        )

        def inject_into(path):
            did = filter_file(r"^#include <R.h>\s*$", "#include <R.h>\n" + insertion, path)
            if did == 0:
                did = filter_file(
                    r"^#include <Rinternals.h>\s$|^#include <Rinternals.h>\s*$",
                    "#include <Rinternals.h>\n" + insertion,
                    path,
                )
            if did == 0:
                # Prepend once at the start of the file
                filter_file(r"\A", insertion, path)

        for relpath in ("src/robustbase.h", "src/lmrob.c"):
            inject_into(relpath)
