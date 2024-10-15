# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchard(RPackage):
    """This package allows one to load scanpy h5ad into R as list, SingleCellExperiment or Seurat object. For now it only loads X, obs, var, obsm (as reduced dimensions) if requested and images for visium data. The package is based on rhdf5 for h5ad manipulation and is pure R (that is reticulate-free)."""

    homepage = "https://www.example.com"
    git = "https://github.com/cellgeni/schard"

    version("2024-10-08", commit="a8f4b03ab7b9f3c182a53510fd12b03be5cee4d1")

    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
