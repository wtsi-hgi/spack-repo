# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiphen(RPackage):
	"""A Package to Test for Multi-Trait Association

	Performs genetic association tests between SNPs
        (one-at-a-time) and multiple phenotypes (separately or in joint
        model).
	"""
	
	cran = "MultiPhen" 

	version("2.0.3", md5="75c888e6eea04d57dde631db98a45031")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-meta", type=("build", "run"))
	depends_on("r-hardyweinberg", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
