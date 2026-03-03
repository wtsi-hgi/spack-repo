# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterflex(RPackage):
	"""Multiplicative Interaction Models Diagnostics and Visualization

	Performs diagnostic tests of multiplicative interaction models and plots non-linear marginal effects of a treatment on an outcome across different values of a moderator.
	"""
	
	homepage = "http://yiqingxu.org/software/interaction/RGuide.html"
	cran = "interflex" 

	version("1.2.6", md5="f43da93ae47989bcd83bd173993d52b2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-sandwich@2.3.4:", type=("build", "run"))
	depends_on("r-lmoments@1.2.3:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-mgcv@1.8.16:", type=("build", "run"))
	depends_on("r-lfe@2.6.2291:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-pcse", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-modelmetrics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
