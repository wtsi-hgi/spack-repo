# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparedf(RPackage):
	"""Do a Git Style Diff of the Rows Between Two Dataframes with
Similar Structure

	Compares two dataframes which have the same column
    structure to show the rows that have changed. Also gives a git style diff format
    to quickly see what has changed in addition to summary statistics.
	"""
	
	cran = "compareDF" 

	version("2.3.5", md5="afa56feee8e1cc940d6045738a108b23")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-htmltable@1.5:", type=("build", "run"))
	depends_on("r-openxlsx@4.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
