# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirmult(RPackage):
	"""Estimation in Dirichlet-Multinomial Distribution

	Estimate parameters in Dirichlet-Multinomial and compute log-likelihoods.
	"""
	
	cran = "dirmult" 

	version("0.1.3-5", md5="253ce25a8287c81ad68a716cd2fe2ab6")

	depends_on("r@2.5:", type=("build", "run"))
