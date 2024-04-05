# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDior(RPackage):
    """The scRNA-seq data IO between R and Python(R version)
    
    The scRNA-seq data IO between R and Python(R version). The scRNA-seq data mainly including the counts, log data,
    cell annotation, gene annotation and dimension reduction can be used to IO via an HDF5 file. In the case of big data, this
    greatly reduces the time of data IO and improves the efficiency of corss-platform scRNA-seq analysis.
    """

    homepage = "https://github.com/JiekaiLab/dior"
    
    git = "https://github.com/JiekaiLab/dior"

    # versions
	version("0.1.5", tag="0.1.5")
    

    # dependencies
    depends_on("r-seurat", type=('build', 'run'))
    depends_on("r-hdf5r", type=('build', 'run'))
    depends_on("r-matrix", type=('build', 'run'))
    depends_on("r-singlecellexperiment", type=('build', 'run'))
    depends_on("r-summarizedexperiment", type=('build', 'run'))
    depends_on("r-hmisc", type=('build', 'run'))
    
