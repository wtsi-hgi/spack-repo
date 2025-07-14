# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiobroom(RPackage):
	"""Turn Bioconductor objects into tidy data frames

	This package contains methods for converting standard objects constructed by bioinformatics packages, especially those in Bioconductor, and converting them to tidy data. It thus serves as a complement to the broom package, and follows the same the tidy, augment, glance division of tidying methods. Tidying data makes it easy to recombine, reshape and visualize bioinformatics analyses.
	"""
	
	homepage = "https://github.com/StoreyLab/biobroom"
	bioc = "biobroom"

	version("1.40.0", commit="e9b0a5ea581dc8083c84ef1405656445d7e5e565")
	version("1.34.0", commit="cd67b426b51963848fbad5e1b4cbe27c91edb694")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
