# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFxtwapls(RPackage):
	"""An Improved Version of WA-PLS

	The goal of this package is to provide an improved version of 
    WA-PLS (Weighted Averaging Partial Least Squares) by including the 
    tolerances of taxa and the frequency of the sampled climate variable. 
    This package also provides a way of leave-out cross-validation that 
    removes both the test site and sites that are both geographically 
    close and climatically close for each cycle, to avoid the risk of 
    pseudo-replication.
	"""
	
	homepage = "https://github.com/special-uor/fxTWAPLS/"
	cran = "fxTWAPLS" 

	version("0.1.2", md5="c20307809e8db001b6c72952a188ce8f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jops", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
