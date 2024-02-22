# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHorm(RPackage):
	"""Supplemental Functions and Datasets for "Handbook of Regression
Methods"

	Supplement for the book "Handbook of Regression Methods" by D. S. Young.  Some datasets used in the book are included and documented.  Wrapper functions are included that simplify the examples in the textbook, such as code for constructing a regressogram and expanding ANOVA tables to reflect the total sum of squares.
	"""
	
	homepage = "https://github.com/dsy109/HoRM"
	cran = "HoRM" 

	version("0.1.3", md5="8153f5293048e50806215d271c80f0db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-rsm", type=("build", "run"))
