# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsdesign2(RPackage):
	"""Group Sequential Design with Non-Constant Effect

	The goal of 'gsDesign2' is to enable fixed or group sequential
    design under non-proportional hazards. To enable highly flexible enrollment,
    time-to-event and time-to-dropout assumptions, 'gsDesign2' offers piecewise
    constant enrollment, failure rates, and dropout rates for a stratified
    population. This package includes three methods for designs:
    average hazard ratio, weighted logrank tests in Yung and Liu (2019)
    <doi:10.1111/biom.13196>, and MaxCombo tests.
    Substantial flexibility on top of what is in the 'gsDesign' package
    is intended for selecting boundaries.
	"""
	
	homepage = "https://merck.github.io/gsDesign2/"
	cran = "gsDesign2" 

	version("1.1.1", md5="64811af20ed0929e07ed5a1a7d657e61", url="https://cran.r-project.org/src/contrib/gsDesign2_1.1.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gsdesign", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-npsurvss", type=("build", "run"))
	depends_on("r-r2rtf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
