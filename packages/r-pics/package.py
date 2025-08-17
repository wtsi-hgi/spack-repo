# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPics(RPackage):
    """Probabilistic inference of ChIP-seq

    Probabilistic inference of ChIP-Seq using an empirical Bayes mixture model approach.
    """

    homepage = "https://github.com/SRenan/PICS"
    bioc = "PICS"

    version("2.52.0", commit="604d4b852085b6587a8aecd82d592aef9a450552")
    version("2.46.0", commit="1638a3ecc20c421e29c3ff2684c8b0ec202f1246")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("gsl", type=("build", "link", "run"))

    # R >= 4.5 removes legacy Calloc/Realloc/Free macros from default headers.
    # Older PICS sources use these macros with a type argument, e.g. Calloc(n, int).
    # Provide compatibility by replacing them with R_Calloc/R_Realloc/R_Free and
    # ensuring the proper memory header is included during compilation.
    def patch(self):
        from glob import glob

        source_files = []
        for pattern in ("src/*.c", "src/*.h"):
            source_files.extend(glob(pattern))

        for src in source_files:
            # Ensure the modern memory API header is available
            filter_file(
                "#include <R.h>",
                "#include <R.h>\n#include <R_ext/Memory.h>",
                src,
            )
            # Fallback: if <R.h> include not present, prepend Memory.h
            filter_file(
                r"^(.*)$",
                "#include <R_ext/Memory.h>\n\\1",
                src,
                string=True,
            )
            # Replace deprecated alloc/free macros with their R_ equivalents
            filter_file(r"\bCalloc\(", "R_Calloc(", src)
            filter_file(r"\bRealloc\(", "R_Realloc(", src)
            filter_file(r"\bFree\(", "R_Free(", src)
