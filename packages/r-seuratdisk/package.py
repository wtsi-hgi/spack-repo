# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeuratdisk(RPackage):
    """Install and Manage Seurat Datasets
    
    Single cell RNA sequencing datasets can be large, consisting of matrices
    that contain expression data for several thousand features across several thousand
    cells. This package is designed to easily install, manage, and learn about various single-cell
    datasets, provided Seurat objects and distributed as independent packages.
    """

    homepage = "https://github.com/mojaveazure/seurat-disk"
    
    git = "https://github.com/mojaveazure/seurat-disk"

    # versions
    version("0.2.2", branch="master")
    

    # dependencies
    depends_on("r@3.5.0:", type=('build', 'run'))
    depends_on("r-hdf5r", type=('build', 'run'))
    depends_on("r-r6", type=('build', 'run'))
    depends_on("r-rlang", type=('build', 'run'))
    depends_on("r-seurat", type=('build', 'run'))
    depends_on("r-seuratobject", type=('build', 'run'))
    depends_on("r-stringi", type=('build', 'run'))
    depends_on("r-withr", type=('build', 'run'))
