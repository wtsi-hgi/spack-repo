# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarselectexposure(RPackage):
	"""Variable Selection Methods Including an Exposure Variable

	Utilizes multiple variable selection methods to estimate Average Treatment Effect.
	"""
	
	cran = "VARSELECTEXPOSURE" 

	version("1.0.3", md5="622253afcd1afee4e91eb7d4a5f87fdb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
