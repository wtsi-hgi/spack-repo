# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtnr(RPackage):
	"""Run Allometric Trophic Networks Models

	Implements the differential equations associated to different versions of Allometric Trophic Models (ATN) to estimate the temporal dynamics of species biomasses in food webs. It offers several features to generate synthetic food webs and to parametrise models as well as a wrapper to the ODE solver deSolve.
	"""
	
	cran = "ATNr" 

	version("1.1.0", md5="5cb6a3ba89e9f0a16c9a4f9ec0ea143b")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-r-rsp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
