# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreatr(RPackage):
	"""Gene Registration from Expression and Time-Courses in R

	A tool for registering (aligning) gene expression profiles
    between two species (reference data and data to transform).
	"""
	
	homepage = "https://ruthkr.github.io/greatR/"
	cran = "greatR" 

	version("1.1.0", md5="68cb456600b13082c1a82ee7d148bbc2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-neldermead", type=("build", "run"))
	depends_on("r-optimization", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
