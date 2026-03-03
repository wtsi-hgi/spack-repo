# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvalue(RPackage):
	"""Sensitivity Analyses for Unmeasured Confounding and Other Biases
in Observational Studies and Meta-Analyses

	Conducts sensitivity analyses for unmeasured confounding, selection bias, and measurement error (individually or in combination; VanderWeele & Ding (2017) <doi:10.7326/M16-2607>; Smith & VanderWeele (2019) <doi:10.1097/EDE.0000000000001032>; VanderWeele & Li (2019) <doi:10.1093/aje/kwz133>; Smith & VanderWeele (2021) <arXiv:2005.02908>). Also conducts sensitivity analyses for unmeasured confounding in meta-analyses (Mathur & VanderWeele (2020a) <doi:10.1080/01621459.2018.1529598>; Mathur & VanderWeele (2020b) <doi:10.1097/EDE.0000000000001180>) and for additive measures of effect modification (Mathur et al., under review).  
	"""
	
	cran = "EValue" 

	version("4.1.3", md5="81b9c995f0ec20e147d5d625f2ec59cf")

	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-metadat", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-metautility", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
