# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXtsum(RPackage):
	"""Summary Statistics for Panel Data

	Based on 'STATA' xtsum command, it is used to compute summary statistics for a panel data set. It generates overall, between-group, and within-group statistics for specified variables in a panel data set, as presented in S. Porter (2023) <https://stephenporter.org/files/xtsum_handout.pdf>, StataCorp (2023) <https://www.stata.com/manuals/xtxtsum.pdf>.
	"""
	
	homepage = "https://github.com/Macosso/xtsum"
	cran = "xtsum" 

	version("0.1.0", md5="e3696306b7f7627fc454b70dc029f5da")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-sampleselection", type=("build", "run"))
