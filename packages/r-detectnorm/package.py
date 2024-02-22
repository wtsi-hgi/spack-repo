# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetectnorm(RPackage):
	"""Detect Nonnormality in Meta-Analysis without Raw Data

	Non-normality could greatly distort the meta-analytic results, according to the simulation in Sun and Cheung (2020) <doi: 10.3758/s13428-019-01334-x>. This package aims to detect non-normality for two independent groups with only limited descriptive statistics, including mean, standard deviation, minimum, and maximum. 
	"""
	
	homepage = "https://github.com/irissun/detectnorm"
	cran = "detectnorm" 

	version("1.0.0", md5="140aa20a77bb2898180c75d8fbe856e8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
