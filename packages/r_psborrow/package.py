# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsborrow(RPackage):
	"""Bayesian Dynamic Borrowing with Propensity Score

	A tool which aims to help evaluate the effect of external borrowing using an integrated approach described in Lewis et al., (2019) <doi:10.1080/19466315.2018.1497533> that combines propensity score and Bayesian dynamic borrowing methods.
	"""
	
	cran = "psborrow" 

	version("0.2.1", md5="5142190f10cfd7199b35127073f16bbe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-matchit", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
