# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcbalance(RPackage):
	"""Large, Sparse Optimal Matching with Refined Covariate Balance

	Tools for large, sparse optimal matching of treated units
	and control units in observational studies.  Provisions are
	made for refined covariate balance constraints, which include
	fine and near-fine balance as special cases.  Matches are 
	optimal in the sense that they are computed as solutions to
	network optimization problems rather than greedy algorithms.
	See Pimentel, et al.(2015) <doi:10.1080/01621459.2014.997879> 
	and Pimentel (2016), Obs. Studies 2(1):4-23. The rrelaxiv 
	package, which provides an alternative solver for
	the underlying network flow problems, carries an
	academic license and is not available on CRAN, but
	may be downloaded from Github at 
	<https://github.com/josherrickson/rrelaxiv/>.
	"""
	
	cran = "rcbalance" 

	version("1.8.8", md5="26c3859b0b590fee57da17f98f4edba2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlemon", type=("build", "run"))
