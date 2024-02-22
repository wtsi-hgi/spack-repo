# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSea(RPackage):
	"""Segregation Analysis

	A few major genes and a series of polygene are responsive for each quantitative trait. Major genes are individually identified while polygene is collectively detected. This is mixed major genes plus polygene inheritance analysis or segregation analysis (SEA). In the SEA, phenotypes from a single or multiple bi-parental segregation populations along with their parents are used to fit all the possible models and the best model of the trait for population phenotypic distributions is viewed as the model of the trait. There are fourteen types of population combinations available. Zhang Yuan-Ming, Gai Jun-Yi, Yang Yong-Hua (2003, <doi:10.1017/S0016672303006141>).
	"""
	
	cran = "SEA" 

	version("2.0.1", md5="20cfde4f7f407dd546342cb203c2b9fa")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-kscorrect", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
