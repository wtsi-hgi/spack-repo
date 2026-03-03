# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobomit(RPackage):
	"""Robustness Checks for Omitted Variable Bias

	Robustness checks for omitted variable bias. The package includes robustness checks proposed by Oster (2019). robomit the estimate i) the bias-adjusted treatment correlation or effect and ii) the degree of selection on unobservables relative to observables (with respect to the treatment variable) that would be necessary to eliminate the result based on the framework by Oster (2019). Additionally, robomit offers a set of sensitivity analysis and visualization functions. See: Oster, E. 2019. <doi:10.1080/07350015.2016.1227711>.
	"""
	
	cran = "robomit" 

	version("1.0.6", md5="2ad54815a6f7ee8c8891aab7cce10a25")

	depends_on("r-plm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
