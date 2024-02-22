# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUncdecomp(RPackage):
	"""Uncertainty Decomposition

	If a procedure consists of several stages and there are several models that can be selected for each stage,
	uncertainty of the procedure can be decomposed by stages or models.
	This package includes the ANOVA-based method, the cumulative uncertainty-based method, and the balanced decomposition method.
	Yongdai Kim et al. (2019) <doi:10.1016/j.hydroa.2019.100024> is a related paper which is accessible via the URL below.
	"""
	
	homepage = "https://www.sciencedirect.com/science/article/pii/S2589915519300082"
	cran = "UncDecomp" 

	version("1.0.1", md5="bcf07c4dd3ee0c090663cf1ef0bdbcaf")

	depends_on("r@3.4.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
