# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnivariateml(RPackage):
	"""Maximum Likelihood Estimation for Univariate Densities

	User-friendly maximum likelihood estimation (Fisher (1921) 
    <doi:10.1098/rsta.1922.0009>) of univariate densities.
	"""
	
	homepage = "https://github.com/JonasMoss/univariateML"
	cran = "univariateML" 

	version("1.1.1", md5="cf7d7127e883f6850e90644d970419fc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-logitnorm", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-nakagami", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
