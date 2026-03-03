# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenchmarkme(RPackage):
	"""Crowd Sourced System Benchmarks

	Benchmark your CPU and compare against other CPUs.  Also
    provides functions for obtaining system specifications, such as RAM,
    CPU type, and R version.
	"""
	
	homepage = "https://github.com/csgillespie/benchmarkme"
	cran = "benchmarkme" 

	version("1.0.8", md5="8b28b0d09ad3727b65a776b15f2024ee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-benchmarkmedata@1.0.4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
