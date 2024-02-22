# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnsmart(RPackage):
	"""Small N Sequential Multiple Assignment Randomized Trial Methods

	Consolidated data simulation, sample size calculation and
    analysis functions for several snSMART (small sample sequential,
    multiple assignment, randomized trial) designs under one library.  See
    Wei, B., Braun, T.M., Tamura, R.N. and Kidwell, K.M. "A Bayesian
    analysis of small n sequential multiple assignment randomized trials
    (snSMARTs)." (2018) Statistics in medicine, 37(26), pp.3723-3732
    <doi:10.1002/sim.7900>.
	"""
	
	homepage = "https://github.com/sidiwang/snSMART"
	cran = "snSMART" 

	version("0.2.3", md5="71acbee0c3951606b3239045a665a6f7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-envstats@2.4:", type=("build", "run"))
	depends_on("r-bayestestr@0.11:", type=("build", "run"))
	depends_on("r-condmvnorm@2020.1:", type=("build", "run"))
	depends_on("r-cubature@2.0.4.1:", type=("build", "run"))
	depends_on("r-geepack@1.3.1:", type=("build", "run"))
	depends_on("r-hdinterval@0.2:", type=("build", "run"))
	depends_on("r-pracma@2.3.3:", type=("build", "run"))
	depends_on("r-rjags@4.12:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-truncdist@1.0.1:", type=("build", "run"))
	depends_on("jags@4:", type=("build", "link", "run"))
