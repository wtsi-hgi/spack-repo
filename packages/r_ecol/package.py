# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcol(RPackage):
	"""Complexity Measures for Supervised Problems

	Provides measures to characterize the complexity of classification 
    and regression problems based on aspects that quantify the linearity of the 
    data, the presence of informative feature, the sparsity and dimensionality 
    of the datasets. This package provides bug fixes, generalizations and 
    implementations of many state of the art measures. The measures are 
    described in the papers: Lorena et al. (2019) <doi:10.1145/3347711> and 
    Lorena et al. (2018) <doi:10.1007/s10994-017-5681-1>.
	"""
	
	homepage = "https://github.com/lpfgarcia/ECoL/"
	cran = "ECoL" 

	version("0.3.0", md5="26795c3a30ea373f6c08d0cfd0e4518c")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
