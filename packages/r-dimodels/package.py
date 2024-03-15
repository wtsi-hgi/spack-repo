# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDimodels(RPackage):
	"""Diversity-Interactions (DI) Models

	The 'DImodels' package is suitable for analysing data from biodiversity and ecosystem function studies using the Diversity-Interactions (DI) modelling approach introduced by Kirwan et al. (2009) <doi:10.1890/08-1684.1>. Suitable data will contain proportions for each species and a community-level response variable, and may also include additional factors, such as blocks or treatments. The package can perform data manipulation tasks, such as computing pairwise interactions (the DI_data() function), can perform an automated model selection process (the autoDI() function) and has the flexibility to fit a wide range of user-defined DI models (the DI() function).
	"""
	
	cran = "DImodels" 

	version("1.3.2", md5="82accf9b0433fda6dc844e92817a22a0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hnp", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
