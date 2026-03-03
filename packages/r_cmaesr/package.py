# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmaesr(RPackage):
	"""Covariance Matrix Adaptation Evolution Strategy

	Pure R implementation of the Covariance Matrix Adaptation -
    Evolution Strategy (CMA-ES) with optional restarts (IPOP-CMA-ES).
	"""
	
	homepage = "https://github.com/jakobbossek/cmaesr"
	cran = "cmaesr" 

	version("1.0.3", md5="8983af258432d9645f82da0e2e17df85")

	depends_on("r-paramhelpers@1.8:", type=("build", "run"))
	depends_on("r-bbmisc@1.6:", type=("build", "run"))
	depends_on("r-checkmate@1.1:", type=("build", "run"))
	depends_on("r-smoof@1.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
