# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcic(RPackage):
	"""Extended Changes-in-Changes

	Extends the Changes-in-Changes model a la Athey and Imbens
    (2006) <doi:10.1111/j.1468-0262.2006.00668.x> to multiple cohorts and
    time periods, which generalizes difference-in-differences estimation
    techniques to the entire distribution. Computes quantile treatment
    effects for every possible two-by-two combination in ecic(). Then,
    aggregating all bootstrap runs adds the standard errors in
    summary_ecic(). Results can be plotted with plot_ecic() aggregated
    over all cohort-group combinations or in an event-study style for
    either individual periods or individual quantiles.
	"""
	
	homepage = "https://frederickluser.github.io/ecic/"
	cran = "ecic" 

	version("0.0.3", md5="fffd67013233b1831501f4b116f1a85f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
