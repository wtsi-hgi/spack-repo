# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaice(RPackage):
	"""Phylogeographic Analysis of Island Colonization Events

	Estimation of the number of colonization events between islands of the same archipelago for a species. It uses rarefaction curves to control for both field and genetic sample sizes as it was described in Coello et al. (2022) <doi:10.1111/jbi.14341>.
	"""
	
	homepage = "<https://github.com/PAICEcode/PAICE>"
	cran = "PAICE" 

	version("1.0.1", md5="885c2cdb08fa609761292c0c3551a776")

	depends_on("r@3.6:", type=("build", "run"))
