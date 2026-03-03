# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLqr(RPackage):
	"""Robust Linear Quantile Regression

	It fits a robust linear quantile regression model using a new family of zero-quantile distributions for the error term. Missing values and censored observations can be handled as well. This family of distribution includes skewed versions of the Normal, Student's t, Laplace, Slash and Contaminated Normal distribution. It also performs logistic quantile regression for bounded responses as shown in Galarza et.al.(2020) <doi:10.1007/s13571-020-00231-0>. It provides estimates and full inference. It also provides envelopes plots for assessing the fit and confidences bands when several quantiles are provided simultaneously.
	"""
	
	cran = "lqr" 

	version("5.0", md5="a90d92efefaf2f2a39c1081d658c83f7")

	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-momtrunc", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
