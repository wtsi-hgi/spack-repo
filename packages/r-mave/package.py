# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMave(RPackage):
	"""Methods for Dimension Reduction

	Functions for dimension reduction, using MAVE (Minimum Average Variance Estimation), OPG (Outer Product of Gradient) and KSIR (sliced inverse regression of kernel version). Methods for selecting the best dimension are also included. Xia (2002) <doi:10.1111/1467-9868.03411>; Xia (2007) <doi:10.1214/009053607000000352>; Wang (2008) <doi:10.1198/016214508000000418>.
	"""
	
	cran = "MAVE" 

	version("1.3.11", md5="9f302d54823ff555990d165607bf1635")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mda", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
