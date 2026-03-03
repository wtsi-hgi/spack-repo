# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSense(RPackage):
	"""Automatic Stacked Ensemble for Regression Tasks

	Stacked ensemble for regression tasks based on 'mlr3' framework with a pipeline for preprocessing numeric and factor features and hyper-parameter tuning using grid or random search.
	"""
	
	homepage = "https://mlr3.mlr-org.com/"
	cran = "sense" 

	version("1.0.0", md5="509ea31da7e47b945f69a9c77dd1725b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mlr3@0.12:", type=("build", "run"))
	depends_on("r-mlr3learners@0.5:", type=("build", "run"))
	depends_on("r-mlr3filters@0.4.2:", type=("build", "run"))
	depends_on("r-mlr3pipelines@0.3.5.1:", type=("build", "run"))
	depends_on("r-mlr3viz@0.5.5:", type=("build", "run"))
	depends_on("r-paradox@0.7.1:", type=("build", "run"))
	depends_on("r-mlr3tuning@0.8:", type=("build", "run"))
	depends_on("r-bbotk@0.3.2:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-forcats@0.5.1:", type=("build", "run"))
	depends_on("r-readr@2.0.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-metrics@0.1.4:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-visnetwork@2.0.9:", type=("build", "run"))
