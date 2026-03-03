# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcmm(RPackage):
	"""Extended Mixed Models Using Latent Classes and Latent Processes

	Estimation of various extensions of the mixed models including latent class mixed models, joint latent class mixed models, mixed models for curvilinear outcomes, mixed models for multivariate longitudinal outcomes using a maximum likelihood estimation method (Proust-Lima, Philipps, Liquet (2017) <doi:10.18637/jss.v078.i02>).
	"""
	
	homepage = "https://cecileproust-lima.github.io/lcmm/"
	cran = "lcmm" 

	version("2.1.0", md5="617131452753c6acf86d88fa87d18233")
	version("2.0.2", md5="402be90b0c3d155bd10f7aa3c972053e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-survival@2.37.2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-marqlevalg@2:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
