# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmc(RPackage):
	"""Phylogenetic Monte Carlo

	Monte Carlo based model choice for applied phylogenetics of
    continuous traits. Method described in  Carl Boettiger, Graham Coop,
    Peter Ralph (2012) Is your phylogeny informative? Measuring
    the power of comparative methods, Evolution 66 (7)
    2240-51. <doi:10.1111/j.1558-5646.2011.01574.x>.
	"""
	
	homepage = "https://github.com/cboettig/pmc"
	cran = "pmc" 

	version("1.0.6", md5="3634b18bf112f3d26f88c59621664436")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geiger@2.0.11:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ouch", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-phytools@1.5.1:", type=("build", "run"))
