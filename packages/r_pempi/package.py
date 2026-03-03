# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPempi(RPackage):
	"""Proportion Estimation with Marginal Proxy Information

	A system contains easy-to-use tools for the conditional estimation of the prevalence of an emerging or rare infectious diseases using the methods proposed in Guerrier et al. (2023) <arXiv:2012.10745>.
	"""
	
	homepage = "https://github.com/stephaneguerrier/pempi"
	cran = "pempi" 

	version("1.0.0", md5="866f81e8dd99f13d391511937fa46d0a")

	depends_on("r@4:", type=("build", "run"))
