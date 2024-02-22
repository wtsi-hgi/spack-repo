# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsaddle(RPackage):
	"""Extended Empirical Saddlepoint Density Approximations

	Tools for fitting the Extended Empirical Saddlepoint (EES) density of Fasiolo et al. (2018) <doi:10.1214/18-EJS1433>.
	"""
	
	homepage = "https://github.com/mfasiolo/esaddle"
	cran = "esaddle" 

	version("0.0.7", md5="eefcecaa09629fe768d5a9f91dd0b555")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
