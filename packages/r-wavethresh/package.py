# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWavethresh(RPackage):
    """Wavelets statistics and transforms."""

    cran = "wavethresh"

    # Minimal version needed by r-confess dependency resolution
    version("4.7.2", sha256="9a9774ca23496df4ecaa2bf9bff345a2ae40ded07f6afd81dd8847d48b43b656")

    # R versions: keep broad; upstream CRAN lists wide compatibility
    depends_on("r@3.0:", type=("build", "run"))
    # CRAN DESCRIPTION lists 'MASS' in Imports
    depends_on("r-mass", type=("build", "run"))

    def patch(self):
        # R 4.5+ may not expose Calloc/Free from R.h; add explicit memory header
        filter_file(
            r"#include\s+<R.h>",
            "#include <R.h>\n#include <R_ext/Memory.h>",
            "src/WAVDE.c",
        )
        # Provide compatibility shims if Calloc/Free are not defined
        filter_file(
            r"#include\s+<stdlib.h>",
            (
                "#include <stdlib.h>\n"
                "#ifndef Calloc\n"
                "#define Calloc(n,t) ((t *)calloc((n), sizeof(t)))\n"
                "#endif\n"
                "#ifndef Free\n"
                "#define Free(p) free(p)\n"
                "#endif\n"
            ),
            "src/WAVDE.c",
        )
