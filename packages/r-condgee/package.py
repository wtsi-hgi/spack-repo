# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondgee(RPackage):
	"""Parameter Estimation in Conditional GEE for Recurrent Event Gap
Times

	Solves for the mean parameters, the variance parameter, and their asymptotic variance in a conditional GEE for recurrent event gap times, as described by Clement and Strawderman (2009) in the journal Biostatistics. Makes a parametric assumption for the length of the censored gap time.
	"""
	
	cran = "condGEE" 

	version("0.2.0", md5="8d7ca585715e193b0bec2f7396b67af6")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
