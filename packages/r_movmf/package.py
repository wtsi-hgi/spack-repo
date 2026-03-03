# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMovmf(RPackage):
	"""Mixtures of von Mises-Fisher Distributions

	Fit and simulate mixtures of von Mises-Fisher distributions.
	"""
	
	cran = "movMF" 

	version("0.2-8", md5="67e466d721c0505edbfef8b9da5a00e9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-skmeans@0.2.10:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-slam@0.1.43:", type=("build", "run"))
