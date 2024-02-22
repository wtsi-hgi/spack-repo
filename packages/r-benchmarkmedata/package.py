# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenchmarkmedata(RPackage):
	"""Data Set for the 'benchmarkme' Package

	Crowd sourced benchmarks from running the
    'benchmarkme' package.
	"""
	
	homepage = "https://github.com/csgillespie/benchmarkme-data"
	cran = "benchmarkmeData" 

	version("1.0.4", md5="09dab4f1d434d65da187689c20dd9261")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
