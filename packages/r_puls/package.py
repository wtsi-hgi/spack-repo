# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPuls(RPackage):
	"""Partitioning Using Local Subregions

	A method of clustering functional data using
    subregion information of the curves. It is intended to supplement the
    'fda' and 'fda.usc' packages in functional data object clustering. It
    also facilitates the printing and plotting of the results in a tree
    format and limits the partitioning candidates into a specific set of
    subregions.
	"""
	
	homepage = "https://vinhtantran.github.io/puls/"
	cran = "puls" 

	version("0.1.2", md5="58d9f9a9e949def68300fb7f020ff3c6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cluster@2.0.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-fda-usc@1.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-monoclust@1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
