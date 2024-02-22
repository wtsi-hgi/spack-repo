# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollin(RPackage):
	"""Visualization the Effects of Collinearity in Distributed Lag
Models and Other Linear Models

	Tool to assessing whether the results of a study could be influenced by
    collinearity. Simulations under a given hypothesized truth regarding effects of an
    exposure on the outcome are used and the resulting curves of lagged effects are
    visualized. A user's manual is provided, which includes detailed examples (e.g. a
    cohort study looking for windows of vulnerability to air pollution, a time series
    study examining the linear association of air pollution with hospital admissions,
    and a time series study examining the non-linear association between temperature and
    mortality). The methods are described in Basagana and Barrera-Gomez (2021) <doi:10.1093/ije/dyab179>.
	"""
	
	cran = "collin" 

	version("0.0.4", md5="8840ff7c489b1000ef9cb34999fd8bfa")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dlnm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
