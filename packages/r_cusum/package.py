# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCusum(RPackage):
	"""Cumulative Sum (CUSUM) Charts for Monitoring of Hospital
Performance

	Provides functions for constructing and evaluating
    CUSUM charts and RA-CUSUM charts with focus on false signal probability. 
	"""
	
	cran = "cusum" 

	version("0.4.1", md5="7017a29174ecbb5b6e33adcac0eaadde")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
