# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3benchmark(RPackage):
	"""Analysis and Visualisation of Benchmark Experiments

	Implements methods for post-hoc analysis and
    visualisation of benchmark experiments, for 'mlr3' and beyond.
	"""
	
	homepage = "https://mlr3benchmark.mlr-org.com"
	cran = "mlr3benchmark" 

	version("0.1.6", md5="2525f6d6fd360a326ef9e1ef8eb7be5f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mlr3misc", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
