# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-sleuth
#
# You can edit this file again by typing:
#
#     spack edit r-sleuth
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RSleuth(RPackage):
    """sleuth is a program for differential analysis of RNA-Seq data."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/pachterlab/sleuth"
    url = "https://github.com/pachterlab/sleuth/archive/refs/tags/v0.30.1.tar.gz"

    license("GPL-3")

    version(
        "0.30.1",
        sha256="4c8efca5d726471cb71187e8db07097a50f63aadf42f6fa25c59e7eed635f982",
    )

    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-lazyeval", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-aggregation", type=("build", "run"))
