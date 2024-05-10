# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScwgcna(RPackage):
    """scWGCNA is an adaptation of WGCNA to work with single-cell datasets."""

    homepage = "https://github.com/CFeregrino/scWGCNA"
    git = "https://github.com/CFeregrino/scWGCNA"

    version("1.1.0", commit="316f28d")

    depends_on("r+X@4.3.2", type=("build", "run"))

    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-ggally", type=("build", "run"))
    depends_on("r-network", type=("build", "run"))
    depends_on("r-sna", type=("build", "run"))
    depends_on("r-dynamictreecut", type=("build", "run"))
    depends_on("r-tinytex", type=("build", "run"))
    depends_on("r-seuratobject", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))

