# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpinow2(RPackage):
	"""Estimate Real-Time Case Counts and Time-Varying Epidemiological
Parameters

	Estimates the time-varying reproduction number,
    rate of spread, and doubling time using a range of open-source tools
    (Abbott et al. (2020) <doi:10.12688/wellcomeopenres.16006.1>), and
    current best practices (Gostic et al. (2020)
    <doi:10.1101/2020.06.18.20134858>).  It aims to help users avoid some
    of the limitations of naive implementations in a framework that is
    informed by community feedback and is actively supported.
	"""
	
	homepage = "https://epiforecasts.io/EpiNow2/"
	cran = "EpiNow2" 

	version("1.4.0", md5="7f39c71d0447eb360b612f82a0663046", url="https://cran.r-project.org/src/contrib/EpiNow2_1.4.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-futile-logger@1.4:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r-utils@2:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-runner", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
