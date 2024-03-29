# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSeuratdata(RPackage):
    """Install and Manage Seurat Datasets
    
    Single cell RNA sequencing datasets can be large, consisting of matrices
    that contain expression data for several thousand features across several thousand
    cells. This package is designed to easily install, manage, and learn about various single-cell
    datasets, provided Seurat objects and distributed as independent packages.
    """

    homepage = "https://github.com/satijalab/seurat-data"
    
    git = "https://github.com/satijalab/seurat-data"

    version("2023-11-04", commit="4dc08e022f51c324bc7bf785b1b5771d2742701d")
    version("0.2.1", tag="v0.2.1")
    
    depends_on("r@3.5.0:", type=('build', 'run'))
    depends_on("r-cli", type=('build', 'run'))
    depends_on("r-crayon", type=('build', 'run'))
    depends_on("r-rappdirs", type=('build', 'run'))
    depends_on("r-seuratobject", type=('build', 'run'))
    depends_on("r-seurat", type=('build', 'run'))
