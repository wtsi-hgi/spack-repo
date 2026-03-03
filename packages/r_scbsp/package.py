# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScbsp(RPackage):
	"""A Fast Tool for Single-Cell Spatially Variable Genes
Identifications on Large-Scale Data

	Identifying spatially variable genes is critical in linking molecular cell functions 
	with tissue phenotypes. This package utilizes a granularity-based dimension-agnostic tool, 
	single-cell big-small patch (scBSP), implementing sparse matrix operation and KD tree 
	method for distance calculation, for the identification of spatially variable genes on 
	large-scale data. The detailed description of this method is available at Wang, J. 
	and Li, J. et al. 2023 (Wang, J. and Li, J. (2023), <doi:10.1038/s41467-023-43256-5>).
	"""
	
	cran = "scBSP" 

	version("0.0.1", md5="6133723667761546fe3b2a54fac362f5")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sparsematrixstats", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
