# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViruslearner(RPackage):
	"""Ensemble Learning for HIV-Related Metrics

	Advanced statistical modeling techniques for ensemble learning, specifically tailored to the analysis of lymphocyte counts and viral load data in the context of HIV research. Empowering researchers and practitioners, this tool provides a comprehensive solution for tasks such as analysis, prediction and risk calculation related to key viral metrics. The package incorporates cutting-edge ensemble learning principles, inspired by model stacking techniques of Simon P. Couch and Max Kuhn (2022) <doi:10.21105/joss.04471> and adhering to tidy data principles, offering a robust and reproducible framework for HIV research.
	"""
	
	homepage = "https://github.com/juanv66x/viruslearner"
	cran = "viruslearner" 

	version("0.0.1", md5="f14e87a80bae14da0a7900549ba6321d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-stacks", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tune", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
	depends_on("r-workflowsets", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
