# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiestim(RPackage):
	"""Estimate Time Varying Reproduction Numbers from Epidemic Curves

	Tools to quantify transmissibility throughout
    an epidemic from the analysis of time series of incidence as described in
    Cori et al. (2013) <doi:10.1093/aje/kwt133> and Wallinga and Teunis (2004) 
    <doi:10.1093/aje/kwh255>.
	"""
	
	homepage = "https://github.com/mrc-ide/EpiEstim"
	cran = "EpiEstim" 

	version("2.2-4", md5="faea8fc1f42b8601a024788ea517e843")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-coarsedatatools@0.6.4:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-incidence@1.7:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
