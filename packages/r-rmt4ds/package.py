# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmt4ds(RPackage):
	"""Computation of Random Matrix Models

	We generate random variables following general Marchenko-Pastur distribution and Tracy-Widom distribution. We compute limits and distributions of eigenvalues and generalized components of spiked covariance matrices. We give estimation of all population eigenvalues of spiked covariance matrix model. We give tests of population covariance matrix. We also perform matrix denoising for signal-plus-noise model.
	"""
	
	cran = "RMT4DS" 

	version("0.0.1", md5="2086c5174c2a3118dff3fb682ca0ea47")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rmtstat", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-mpoly", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
