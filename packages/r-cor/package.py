# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCor(RPackage):
	"""The COR for Optimal Subset Selection in Distributed Estimation

	An algorithm of optimal subset selection, related to Covariance matrices, 
 Observation matrices and Response vectors (COR) to select the optimal subsets
 in distributed estimation. The philosophy of the package is described in Guo G. (2020) <doi:10.1080/02331888.2020.1823979>. 
	"""
	
	cran = "COR" 

	version("0.0.1", md5="630cc70c9d1667f3bc9c412ead2e80ba")

	depends_on("r@3.5:", type=("build", "run"))
