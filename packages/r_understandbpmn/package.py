# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnderstandbpmn(RPackage):
	"""Calculator of Understandability Metrics for BPMN

	Calculate several understandability metrics of BPMN models. BPMN stands for business process modelling notation and is a language for expressing business processes into business process diagrams. Examples of these understandability metrics are: average connector degree, maximum connector degree, sequentiality, cyclicity, diameter, depth, token split, control flow complexity, connector mismatch, connector heterogeneity, separability, structuredness and cross connectivity. See R documentation and paper on metric implementation included in this package for more information concerning the metrics.
	"""
	
	cran = "understandBPMN" 

	version("1.1.1", md5="4b3752e6a25e3132ec0753189c3c6879")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
