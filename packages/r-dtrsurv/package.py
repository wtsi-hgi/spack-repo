# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtrsurv(RPackage):
	"""Dynamic Treatment Regimes for Survival Analysis

	Provides methods for estimating multi-stage optimal dynamic treatment regimes for survival outcomes with dependent censoring. Cho, H., Holloway, S. T., and Kosorok, M. R. (2020) <arXiv:2012.03294>.
	"""
	
	cran = "dtrSurv" 

	version("1.4", md5="ba687d321c195b28210b2b826502da9c")

	depends_on("r-survival", type=("build", "run"))
