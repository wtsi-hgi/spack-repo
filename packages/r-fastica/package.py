# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastica(RPackage):
    """FastICA Algorithms to Perform ICA and Projection Pursuit.

    Implementation of FastICA algorithm to perform Independent Component
    Analysis (ICA) and Projection Pursuit."""

    cran = "fastICA"
    version("1.2-4", md5="0cc1a6b1e7c27d7c410cdfb0f0cb9e5a")
    version("1.2-3", sha256="e9ef82644cb64bb49ae3b7b6e0885f4fb2dc08ae030f8c76fe8dd8507b658950")
    version("1.2-2", sha256="32223593374102bf54c8fdca7b57231e4f4d0dd0be02d9f3500ad41b1996f1fe")

    depends_on("r@4:", type=("build", "run"))

    # R >= 4.4 removed legacy Calloc/Free macros from the default headers.
    # Inject a tiny compatibility header and force-include it during build.
    def setup_build_environment(self, env):
        env.append_flags(
            "PKG_CPPFLAGS",
            "-include R_ext/RS.h -include R_ext/Memory.h -include spack_compat.h",
        )

    def patch(self):
        import os

        src_dir = os.path.join("src")
        os.makedirs(src_dir, exist_ok=True)
        compat_h = os.path.join(src_dir, "spack_compat.h")
        compat_contents = (
            "#ifndef SPACK_R_FASTICA_COMPAT_H\n"
            "#define SPACK_R_FASTICA_COMPAT_H\n"
            "#include <R.h>\n"
            "#include <R_ext/Memory.h>\n"
            "#ifndef Calloc\n"
            "#define Calloc(n,t) ((t*) R_chk_calloc((size_t)(n), sizeof(t)))\n"
            "#endif\n"
            "#ifndef Realloc\n"
            "#define Realloc(p,n,t) ((t*) R_chk_realloc((void*)(p), (size_t)(n) * sizeof(t)))\n"
            "#endif\n"
            "#ifndef Free\n"
            "#define Free(p) R_chk_free((void*)(p))\n"
            "#endif\n"
            "#endif /* SPACK_R_FASTICA_COMPAT_H */\n"
        )
        with open(compat_h, "w", encoding="utf-8") as f:
            f.write(compat_contents)
