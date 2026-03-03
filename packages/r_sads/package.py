# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSads(RPackage):
	"""Maximum Likelihood Models for Species Abundance Distributions

	Maximum likelihood tools to fit and compare models of species
    abundance distributions and of species rank-abundance distributions.
	"""
	
	homepage = "https://github.com/piLaboratory/sads"
	cran = "sads" 

	version("0.6.3", md5="bb68c35c6279e3f78550a335cd96f866")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bbmle@1.0.19:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-poilog", type=("build", "run"))
	depends_on("r-guilds", type=("build", "run"))
	depends_on("r-powerlaw", type=("build", "run"))
