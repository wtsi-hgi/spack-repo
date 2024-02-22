# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTernGee(RPackage):
	"""Tables and Graphs for Generalized Estimating Equations (GEE)
Model Fits

	Generalized estimating equations (GEE) are a popular choice for analyzing 
  longitudinal binary outcomes. This package provides an interface for fitting GEE,
  currently for logistic regression, within the 'tern' <https://cran.r-project.org/package=tern> 
  framework (Zhu, Sabanés Bové et al., 2023) and tabulate results easily using
  'rtables' <https://cran.r-project.org/package=rtables> (Becker, Waddell et al., 2023).
  It builds on 'geepack' <doi:10.18637/jss.v015.i02> (Højsgaard, Halekoh and Yan, 2006) 
  for the actual GEE model fitting.
	"""
	
	homepage = "https://github.com/insightsengineering/tern.gee/"
	cran = "tern.gee" 

	version("0.1.3", md5="ab59ec763dbcd0d68caed831e8ebd15d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tern@0.9.3:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-emmeans@1.4.5:", type=("build", "run"))
	depends_on("r-formatters@0.5.5:", type=("build", "run"))
	depends_on("r-geeasy", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rtables@0.6.6:", type=("build", "run"))
