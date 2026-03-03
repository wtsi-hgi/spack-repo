# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiproperm(RPackage):
	"""Conduct Direction-Projection-Permutation Tests and Display Plots

	Conducts a direction-projection-permutation test and displays diagnostic plots to facilitate the visual assessment of the test. See Wei et al. (2016) <doi:10.1080/10618600.2015.1027773> and Lam et al. (2018) <doi:10.1080/10618600.2017.1366915> for more details.
	"""
	
	cran = "diproperm" 

	version("0.2.0", md5="76bd372f269cf9ff43439e947ec7c863")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lemon", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dwdlarger", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
