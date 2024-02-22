# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvidinri(RPackage):
	"""IDI and NRI for Comparing Competing Risk Prediction Models with
Censored Survival Data

	Performs inference for a class of measures to compare competing risk prediction models with censored survival data. The class includes the integrated discrimination improvement index (IDI) and category-less net reclassification index (NRI).
	"""
	
	cran = "survIDINRI" 

	version("1.1-2", md5="4cb80c5409468ad759e0443a0a364e00")

	depends_on("r-survc1", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
