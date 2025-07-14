# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepstat(RPackage):
	"""Statistical analysis of peptide microarrays

	Statistical analysis of peptide microarrays
	"""
	
	homepage = "https://github.com/RGLab/pepStat"
	bioc = "pepStat"

	version("1.42.0", commit="59eae09101f2c1af0951c71bbebba8db5aa4f014")
	version("1.36.0", commit="d5c36a6d90d55618c08b469e58848424968b1b2f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
