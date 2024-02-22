# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValr(RPackage):
	"""Genome Interval Arithmetic

	Read and manipulate genome intervals and signals. Provides
    functionality similar to command-line tool suites within R, enabling
    interactive analysis and visualization of genome-scale data.  Riemondy
    et al. (2017) <doi:10.12688/f1000research.11997.1>.
	"""
	
	homepage = "https://github.com/rnabioco/valr/"
	cran = "valr" 

	version("0.7.0", md5="db3d0884464d8a9ed555293b4dd7d4d4")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
