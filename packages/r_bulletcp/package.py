# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBulletcp(RPackage):
	"""Automatic Groove Identification via Bayesian Changepoint
Detection

	Provides functionality to automatically detect groove locations via a Bayesian changepoint detection method to be used in the data preprocessing step
    of forensic bullet matching algorithms. The methods in this package are based on those in Stephens (1994) <doi:10.2307/2986119>. Bayesian changepoint detection will simply be an option
    in the function from the package 'bulletxtrctr' which identifies the groove locations.
	"""
	
	cran = "bulletcp" 

	version("1.0.0", md5="64df9dce21046755197cf389a234ac16")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
