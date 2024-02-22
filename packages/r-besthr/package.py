# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBesthr(RPackage):
	"""Generating Bootstrap Estimation Distributions of HR Data

	Creates plots showing scored HR experiments and plots of distribution of
    means of ranks of HR score from bootstrapping. Authors (2019) <doi:10.5281/zenodo.3374507>.
	"""
	
	cran = "besthr" 

	version("0.3.2", md5="53bb0d72990c4b45e996faec27144da7")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
