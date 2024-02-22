# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRater(RPackage):
	"""Statistical Models of Repeated Categorical Rating Data

	Fit statistical models based on the Dawid-Skene model - Dawid
    and Skene (1979) <doi:10.2307/2346806> - to repeated categorical
    rating data.  Full Bayesian inference for these models is supported
    through the Stan modelling language. 'rater' also allows the user to
    extract and plot key parameters of these models.
	"""
	
	homepage = "https://jeffreypullin.github.io/rater/"
	cran = "rater" 

	version("1.3.1", md5="2ba733a31ee7a73292e8e2f8660c9572")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-loo@2:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
