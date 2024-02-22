# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrailtyem(RPackage):
	"""Fitting Frailty Models with the EM Algorithm

	Contains functions for fitting shared frailty models with a semi-parametric
    baseline hazard with the Expectation-Maximization algorithm. Supported data formats 
    include clustered failures with left truncation and recurrent events in gap-time
    or Andersen-Gill format. Several frailty distributions, such as the the gamma, positive stable
    and the Power Variance Family are supported. 
	"""
	
	homepage = "https://github.com/tbalan/frailtyEM"
	cran = "frailtyEM" 

	version("1.0.1", md5="7e1c67374cd3aa7af2f9c08c54acf324")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-expint", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
