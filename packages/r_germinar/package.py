# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGerminar(RPackage):
	"""Indices and Graphics for Assess Seed Germination Process

	A collection of different indices and visualization techniques for evaluate the seed germination process in ecophysiological studies (Lozano-Isla et al. 2019) <doi:10.1111/1440-1703.1275>.
	"""
	
	homepage = "https://germinar.inkaverse.com/"
	cran = "GerminaR" 

	version("2.1.4", md5="249fcdbefcde6182461b5863395e3722")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
