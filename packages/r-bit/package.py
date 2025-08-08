# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack.package import *


class RBit(RPackage):
    """Class for vectors of bits.

    Provides bitmapped vectors of booleans (no NAs), coercion from and to
    logicals, integers and integer subscripts, fast boolean operators and
    fast summary statistics. With 'bit' class you can store true binary
    booleans 'at the price of' one bit only, on a 32 bit architecture that
    makes 32 times less RAM and cache miss and even more on 64 bit
    architecture. Due to 'bit's special coercion code, you can convert
    booleans to integers and vice versa without any memory overhead.
    'bit' has some limitations, for example you cannot assign names to bit
    vectors and they cannot be used as keys in hash tables. Other than that
    'bit' aims to be as compatible as possible with R's logical vectors.
    """

    cran = "bit"

    # Include the version needed by our concretization
    version("4.0.5", sha256="f0f2536a8874b6a30b80baefbc68cb21f0ffbf51f3877bda8038c3f9f354bfbc")

    depends_on("r@2.9:", type=("build", "run"))

    def patch(self):
        # Some older sources use Calloc/Free macros which are hidden under
        # STRICT_R_HEADERS with R >= 4.5. Inject safe fallbacks in bit.c.
        src_dir = join_path(self.stage.source_path, "src")
        if os.path.isdir(src_dir):
            prelude_marker = "/* spack-prelude-injected */\n"
            prelude = (
                prelude_marker
                + "#include <stdlib.h>\n"
                + "#ifndef Calloc\n"
                + "#define Calloc(n,t) (t *) calloc((size_t)(n), sizeof(t))\n"
                + "#endif\n"
                + "#ifndef Free\n"
                + "#define Free(p) free(p)\n"
                + "#endif\n"
            )
            # Apply to all C sources that might reference Calloc/Free
            for name in os.listdir(src_dir):
                if not name.endswith(".c"):
                    continue
                file_path = join_path(src_dir, name)
                with open(file_path, "r", encoding="utf-8") as f:
                    original = f.read()
                if prelude_marker in original:
                    continue
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(prelude + original)
