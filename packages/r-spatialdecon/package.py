# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialdecon(RPackage):
    """Deconvolution of mixed cells from spatial and/or bulk gene expression data

    Using spatial or bulk gene expression data, estimates abundance of mixed cell types within each observation. Based on "Advances in mixed cell deconvolution enable quantification of cell types in spatial transcriptomic data", Danaher (2022). Designed for use with the NanoString GeoMx platform, but applicable to any gene expression data.
    """

    bioc = "SpatialDecon"

    version("1.18.0", commit="8fa5b25a34b74c9b5fb51eae38cd5d0d67a92f31")
    version("1.12.3", commit="9108acd89a3cd950a690d115f402e12b641739de")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-seuratobject", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-geomxtools", type=("build", "run"))
    depends_on("r-repmis", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-lognormreg@0.4:", type=("build", "run"))
