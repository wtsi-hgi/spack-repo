# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpcs(RPackage):
	"""Neyman-Pearson Classification via Cost-Sensitive Learning

	We connect the multi-class Neyman-Pearson classification (NP) problem to the cost-sensitive learning (CS) problem, and propose two algorithms (NPMC-CX and NPMC-ER) to solve the multi-class NP problem through cost-sensitive learning tools. Under certain conditions, the two algorithms are shown to satisfy multi-class NP properties. More details are available in the paper "Neyman-Pearson Multi-class Classification via Cost-sensitive Learning" (Ye Tian and Yang Feng, 2021).
	"""
	
	cran = "npcs" 

	version("0.1.1", md5="51dad4519b2b32223159160fbec97c4d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-smotefamily", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
