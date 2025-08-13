# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeriation(RPackage):
    """Infrastructure for Ordering Objects Using Seriation

    Infrastructure for ordering objects with an implementation of several
    seriation/sequencing/ordination techniques to reorder matrices, dissimilarity
    matrices, and dendrograms. Also provides (optimally) reordered heatmaps,
    color images and clustering visualizations like dissimilarity plots, and
    visual assessment of cluster tendency plots (VAT and iVAT). Hahsler et al (2008) <doi:10.18637/jss.v025.i03>.
    """

    homepage = "https://github.com/mhahsler/seriation"
    cran = "seriation"

    version("1.5.4", md5="e44c7b7bfe1340609df38646cbdccf3c")

    # Fix build with R >= 4.5 where Calloc/Free moved to R_ext/Memory.h
    # and require explicit includes/macros. We inject compatibility macros
    # directly in the patch() method below.

    def patch(self):
        insertion = (
            "#include <R_ext/Memory.h>\n"
            "#ifndef Calloc\n"
            "#define Calloc(n, T) R_Calloc((n), T)\n"
            "#endif\n"
            "#ifndef Free\n"
            "#define Free(p) R_Free(p)\n"
            "#endif\n"
        )

        for relpath in ["src/optimal.c", "src/stress.c"]:
            # Read file content
            with open(relpath, "r", encoding="utf-8") as f:
                content = f.read()

            # Skip if we've already inserted
            if "R_ext/Memory.h" in content and "#ifndef Calloc" in content:
                continue

            new_content = content
            if "#include <Rinternals.h>" in content:
                new_content = content.replace(
                    "#include <Rinternals.h>",
                    "#include <Rinternals.h>\n" + insertion,
                    1,
                )
            elif "#include <R.h>" in content:
                new_content = content.replace(
                    "#include <R.h>",
                    "#include <R.h>\n" + insertion,
                    1,
                )
            else:
                # Prepend as a last resort
                new_content = insertion + content

            with open(relpath, "w", encoding="utf-8") as f:
                f.write(new_content)

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-ca", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-gclus", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-qap", type=("build", "run"))
    depends_on("r-registry", type=("build", "run"))
    depends_on("r-tsp", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
