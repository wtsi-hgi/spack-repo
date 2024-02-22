# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViraldomain(RPackage):
	"""Applicability Domain Methods of Viral Load and CD4 Lymphocytes

	Provides methods for assessing the applicability domain of models that predict viral load and CD4 (Cluster of Differentiation 4) lymphocyte counts. These methods help determine the extent of extrapolation when making predictions.
	"""
	
	cran = "viraldomain" 

	version("0.0.3", md5="f2aff334e04a22b0ffc588614e9d4339")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-applicable", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-vdiffr", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
