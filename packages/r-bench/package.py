# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBench(RPackage):
	"""High Precision Timing of R Expressions

	Tools to accurately benchmark and analyze execution times for
    R expressions.
	"""
	
	homepage = "https://bench.r-lib.org/"
	cran = "bench" 

	version("1.1.3", md5="43e8d84281622523ae407aa0c4f31556")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-pillar@1.9:", type=("build", "run"))
	depends_on("r-profmem@0.6:", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
