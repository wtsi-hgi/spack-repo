# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcwr(RPackage):
	"""Acute Chronic Workload Ratio Calculation

	Functions for calculating the acute chronic workload ratio using three 
            different methods: exponentially weighted moving average (EWMA), rolling 
            average coupled (RAC) and rolling averaged uncoupled (RAU). Examples of this 
            methods can be found in Williams et al. (2017) <doi:10.1136/bjsports-2016-096589>
            for EWMA and Windt & Gabbet (2018) for RAC and RAU <doi: 10.1136/bjsports-2017-098925>.
	"""
	
	homepage = "https://github.com/JorgeDelro/ACWR"
	cran = "ACWR" 

	version("0.1.0", md5="95507e246c5db5ddf6258f89fc5c2960")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r2d3", type=("build", "run"))
