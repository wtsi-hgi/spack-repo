# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesboot(RPackage):
	"""An Implementation of Rubin's (1981) Bayesian Bootstrap

	Functions for performing the Bayesian bootstrap as introduced by
    Rubin (1981) <doi:10.1214/aos/1176345338> and for summarizing the result.
    The implementation can handle both summary statistics that works on a
    weighted version of the data and summary statistics that works on a
    resampled data set.
	"""
	
	homepage = "https://github.com/rasmusab/bayesboot"
	cran = "bayesboot" 

	version("0.2.2", md5="7e2648cc93c4661a4fe9dcdf91594202")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-hdinterval@0.1.1:", type=("build", "run"))
