# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrought(RPackage):
	"""Statistical Modeling and Assessment of Drought

	Provide tools for drought monitoring based on univariate and multivariate drought indicators.Statistical drought prediction based on Ensemble Streamflow Prediction (ESP), drought risk assessments, and drought propagation are also provided. Please see Hao Zengchao et al. (2017) <doi:10.1016/j.envsoft.2017.02.008>.
	"""
	
	cran = "drought" 

	version("1.1", md5="e96edc5ceb2cc8dfe8b631997cbaa23b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
