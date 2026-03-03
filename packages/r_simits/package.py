# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimits(RPackage):
	"""Analysis via Simulation of Interrupted Time Series (ITS) Data

	Uses simulation to create prediction intervals for
    post-policy outcomes in interrupted time series (ITS) designs,
    following Miratrix (2020) <arXiv:2002.05746>. This package provides
    methods for fitting ITS models with lagged outcomes and variables to
    account for temporal dependencies.  It then conducts inference via
    simulation, simulating a set of plausible counterfactual post-policy
    series to compare to the observed post-policy series. This package
    also provides methods to visualize such data, and also to incorporate
    seasonality models and smoothing and aggregation/summarization.  This
    work partially funded by Arnold Ventures in collaboration with
    MDRC.
	"""
	
	cran = "simITS" 

	version("0.1.1", md5="e93fd00e9c6f0f21d10f41b161ec78af")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
