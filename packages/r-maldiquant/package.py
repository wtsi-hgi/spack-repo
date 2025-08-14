# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaldiquant(RPackage):
    """Quantitative Analysis of Mass Spectrometry Data.

    A complete analysis pipeline for matrix-assisted laser
    desorption/ionization-time-of-flight (MALDI-TOF) and other two-dimensional
    mass spectrometry data. In addition to commonly used plotting and
    processing methods it includes distinctive features, namely baseline
    subtraction methods such as morphological filters (TopHat) or the
    statistics-sensitive non-linear iterative peak-clipping algorithm (SNIP),
    peak alignment using warping functions, handling of replicated measurements
    as well as allowing spectra with different resolutions."""

    cran = "MALDIquant"
    version("1.22.2", sha256="6051b07019003c698ae016d79f13945bfe2edec26f8a688126b978cb90adcfff")
    version("1.22.1", sha256="0a52a55dbe76a7e7ca50c5555fea4381eeda0c215c66e420d8dc9bfd2992411c")
    version("1.21", sha256="0771f82034aa6a77af67f3572c900987b7e6b578d04d707c6e06689d021a2ff8")
    version("1.19.3", sha256="a730327c1f8d053d29e558636736b7b66d0671a009e0004720b869d2c76ff32c")
    version("1.19.2", sha256="8c6efc4ae4f1af4770b079db29743049f2fd597bcdefeaeb16f623be43ddeb87")
    version("1.16.4", sha256="9b910dbd5dd1a739a17a7ee3f83d7e1ebad2fee89fd01a5b274415d2b6d3b0de")

    depends_on("r@4:", type=("build", "run"))

    # R 4.5 removed legacy Calloc/Free macros. Provide compatibility shim.
    # Inject compatibility macros into the package header at patch time so all
    # C files get the definitions.
    def patch(self):
        import os

        def inject_macros_in_file(file_path: str) -> bool:
            if not os.path.exists(file_path):
                return False
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Prefer placing right after R headers
            insertion_anchor = "#include <Rinternals.h>"
            compat_block = (
                "#include <Rinternals.h>\n"
                "#include <R_ext/Memory.h>\n"
                "#include <Rversion.h>\n"
                "#ifndef Calloc\n"
                "#define Calloc(n, T) (T*) R_Calloc((n), T)\n"
                "#endif\n"
                "#ifndef Free\n"
                "#define Free(p) R_Free(p)\n"
                "#endif\n"
            )

            if compat_block in content:
                return True  # already injected

            if insertion_anchor in content:
                new_content = content.replace(insertion_anchor, compat_block)
            else:
                # Fallback: prepend to the file to guarantee availability
                new_content = compat_block + content

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True

        # In CRAN tarballs, C sources live under top-level 'src/'
        src_dir = os.path.join(self.stage.source_path, "src")
        header_path = os.path.join(src_dir, "MALDIquant.h")
        c_file_path = os.path.join(src_dir, "lowerConvexHull.c")

        # Try the canonical header first, then the specific C file as fallback
        changed = inject_macros_in_file(header_path)
        if not changed:
            inject_macros_in_file(c_file_path)
