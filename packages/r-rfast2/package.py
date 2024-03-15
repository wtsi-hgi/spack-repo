# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfast2(RPackage):
	"""A Collection of Efficient and Extremely Fast R Functions II

	A collection of fast statistical and utility functions for data analysis. Functions for regression, maximum likelihood, column-wise statistics and many more have been included. C++ has been utilized to speed up the functions. References: Tsagris M., Papadakis M. (2018). Taking R to its limits: 70+ tips. PeerJ Preprints 6:e26605v1 <doi:10.7287/peerj.preprints.26605v1>.
	"""
	
	homepage = "https://github.com/RfastOfficial/Rfast2"
	cran = "Rfast2" 

	version("0.1.5.2", md5="d455cceffbdcf6e19bf117726ce34ba4", url="https://cran.r-project.org/src/contrib/Rfast2_0.1.5.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12.3:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rnanoflann", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
