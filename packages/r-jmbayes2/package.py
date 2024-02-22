# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmbayes2(RPackage):
	"""Extended Joint Models for Longitudinal and Time-to-Event Data

	Fit joint models for longitudinal and time-to-event data under the Bayesian approach. Multiple longitudinal outcomes of mixed type (continuous/categorical) and multiple event times (competing risks and multi-state processes) are accommodated. Rizopoulos (2012, ISBN:9781439872864).
	"""
	
	homepage = "https://drizopoulos.github.io/JMbayes2/"
	cran = "JMbayes2" 

	version("0.4-5", md5="89426c7585449394deece65eb4d370c5", url="https://cran.r-project.org/src/contrib/JMbayes2_0.4-5.tar.gz")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-glmmadaptive", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
