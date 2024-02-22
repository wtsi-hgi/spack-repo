# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutorasch(RPackage):
	"""Semi-Automated Rasch Analysis

	Performs Rasch analysis (semi-)automatically, which has been shown to be comparable with the standard Rasch analysis (Feri Wijayanto et al. (2021) <doi:10.1111/bmsp.12218>, Feri Wijayanto et al. (2022) <doi:10.3758/s13428-022-01947-9>, Feri Wijayanto et al. (2022) <doi:10.1177/01466216221125178>).
	"""
	
	cran = "autoRasch" 

	version("0.2.2", md5="f9edb3fe8db360bf3a91847a00cb745f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
