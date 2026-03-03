# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyspia(RPackage):
	"""Dysregulated Pathway Identification Analysis

	It is used to identify dysregulated pathways based on a pre-ranked gene pair list. A fast algorithm is used to make the computation really fast. The data in package 'DysPIAData' is needed.
	"""
	
	cran = "DysPIA" 

	version("1.3", md5="b820212232bf8513530a68aed26fc31c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dyspiadata", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-parmigene", type=("build", "run"))
