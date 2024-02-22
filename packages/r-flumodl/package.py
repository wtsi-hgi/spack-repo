# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlumodl(RPackage):
	"""Influenza-Attributable Mortality with Distributed-Lag Models

	Functions to estimate the mortality attributable to 
    influenza and temperature, using distributed-lag nonlinear models
    (DLNMs), as first implemented in 
    Lytras et al. (2019) <doi:10.2807/1560-7917.ES.2019.24.14.1800118>.
    Full descriptions of underlying DLNM methodology in Gasparrini et al. 
    <doi:10.1002/sim.3940> (DLNMs), 
    <doi:10.1186/1471-2288-14-55> (attributable risk from DLNMs) and 
    <doi:10.1002/sim.5471> (multivariate meta-analysis).
	"""
	
	cran = "FluMoDL" 

	version("0.0.3", md5="6945df010b1b63a8f8d7d53c1dd9213b")

	depends_on("r-dlnm", type=("build", "run"))
	depends_on("r-mvmeta", type=("build", "run"))
	depends_on("r-tsmodel", type=("build", "run"))
