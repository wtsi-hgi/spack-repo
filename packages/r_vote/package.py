# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVote(RPackage):
	"""Election Vote Counting

	Counting election votes and determining election results by different methods, including
    the single transferable vote or ranked choice, approval, score, plurality, condorcet and two-round runoff methods (Raftery et al., 2021 <doi:10.32614/RJ-2021-086>).
	"""
	
	cran = "vote" 

	version("2.4-3", md5="5e124b592e48d2aff7eed91668651040")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
