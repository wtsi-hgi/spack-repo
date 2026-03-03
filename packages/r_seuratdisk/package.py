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

    version("0.0.0.9015", commit="877d4e18ab38c686f5db54f8cd290274ccdbe295")
    
    depends_on("r@3.5.0:", type=('build', 'run'))
    depends_on("r-cli", type=('build', 'run'))
    depends_on("r-crayon", type=('build', 'run'))
    depends_on("r-rappdirs", type=('build', 'run'))
    depends_on("r-matrix", type=('build', 'run'))
    depends_on("r-seuratdata", type=('build', 'run'))
    depends_on("r-seurat", type=('build', 'run'))
    depends_on("r-hdf5r", type=('build', 'run'))
