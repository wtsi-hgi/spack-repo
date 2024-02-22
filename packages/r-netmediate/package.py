# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetmediate(RPackage):
	"""Micro-Macro Analysis for Social Networks

	Estimates micro effects on macro structures (MEMS) and average micro mediated effects (AMME).
    URL: <https://github.com/sduxbury/netmediate>.
    BugReports: <https://github.com/sduxbury/netmediate/issues>.
    Robins, Garry, Phillipa Pattison, and Jodie Woolcock (2005) <doi:10.1086/427322>.
    Snijders, Tom A. B., and Christian E. G. Steglich (2015) <doi:10.1177/0049124113494573>.
    Imai, Kosuke, Luke Keele, and Dustin Tingley (2010) <doi:10.1037/a0020761>.
    Duxbury, Scott (2023) <doi:10.1177/00811750231209040>.
    Duxbury, Scott (2024) <doi:10.1177/00811750231220950>.
	"""
	
	cran = "netmediate" 

	version("0.1.4", md5="40e25e3c2cb68fbf400167c0fd2bb801")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-btergm", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-rsiena", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ergmargins", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
