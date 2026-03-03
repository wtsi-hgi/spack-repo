# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIohexperimenter(RPackage):
	"""Benchmarking Part of the 'IOHprofiler'

	The benchmarking module for the Iterative Optimization Heuristics
    Profiler ('IOHprofiler'). This module provides benchmarking in the 'IOHprofiler'
    format, which can be visualized using the 'IOHanalyzer' module.
	"""
	
	homepage = "https://github.com/IOHprofiler/IOHexperimenter"
	cran = "IOHexperimenter" 

	version("0.1.4", md5="5e6602bec26405266e26ce60773a1d95")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
