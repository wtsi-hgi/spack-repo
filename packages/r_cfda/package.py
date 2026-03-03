# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfda(RPackage):
	"""Categorical Functional Data Analysis

	Package for the analysis of categorical functional data.
  The main purpose is to compute an encoding (real functional variable) for each state <doi:10.3390/math9233074>.
  It also provides functions to perform basic statistical analysis on categorical functional data.
	"""
	
	homepage = "https://modal-inria.github.io/cfda/"
	cran = "cfda" 

	version("0.11.0", md5="145257da7502d46bb08735168b4d17d2")

	depends_on("r-fda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
