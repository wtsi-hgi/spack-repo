# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcbsubset(RPackage):
	"""Optimal Subset Matching with Refined Covariate Balance

	Tools for optimal subset matching of treated units
	and control units in observational studies, with support
	for refined covariate balance constraints, (including
	fine and near-fine balance as special cases). A close 
	relative is the 'rcbalance' package.  See Pimentel, 
	et al.(2015) <doi:10.1080/01621459.2014.997879>
	and Pimentel and Kelz (2020) 
	<doi:10.1080/01621459.2020.1720693>. The rrelaxiv 
	package, which provides an alternative solver for
	the underlying network flow problems, carries an
	academic license and is not available on CRAN, but
	may be downloaded from Github at 
	<https://github.com/josherrickson/rrelaxiv/>.
	"""
	
	cran = "rcbsubset" 

	version("1.1.7", md5="ea0affe1c5b5f083f5713ee6abb70dc8")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcbalance", type=("build", "run"))
	depends_on("r-rlemon", type=("build", "run"))
