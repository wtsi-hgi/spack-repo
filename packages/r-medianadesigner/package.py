# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedianadesigner(RPackage):
	"""Power and Sample Size Calculations for Clinical Trials

	
  Efficient simulation-based power and sample size calculations are supported for a
  broad class of late-stage clinical trials. The following modules are included in
  the package:
  Adaptive designs with data-driven sample size or event count re-estimation,
  Adaptive designs with data-driven treatment selection,
  Adaptive designs with data-driven population selection,
  Optimal selection of a futility stopping rule,
  Event prediction in event-driven trials,
  Adaptive trials with response-adaptive randomization (experimental module),
  Traditional trials with multiple objectives (experimental module).
  Traditional trials with cluster-randomized designs (experimental module).
	"""
	
	homepage = "https://github.com/medianasoft/MedianaDesigner"
	cran = "MedianaDesigner" 

	version("0.13", md5="baa934d003d5f744e18e604681a9b05b")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-devemf", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinymatrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-pbkrtest", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
