# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLexisnexistools(RPackage):
	"""Working with Files from 'LexisNexis'

	My PhD supervisor once told me that everyone doing newspaper
    analysis starts by writing code to read in files from the 'LexisNexis' newspaper
    archive (retrieved e.g., from <https://www.lexisnexis.com/> or any of the partner
    sites). However, while this is a nice exercise I do recommend, not everyone has
    the time. This package takes files downloaded from the newspaper archive of
    'LexisNexis', reads them into R and offers functions for further processing.
	"""
	
	homepage = "https://github.com/JBGruber/LexisNexisTools"
	cran = "LexisNexisTools" 

	version("0.3.7", md5="b7b0bf2ff0bcdca56a1aa5611a58af21")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-pbapply@1.3.4:", type=("build", "run"))
	depends_on("r-quanteda@1.1:", type=("build", "run"))
	depends_on("r-quanteda-textstats", type=("build", "run"))
	depends_on("r-stringdist@0.9.4:", type=("build", "run"))
	depends_on("r-stringi@1.1.7:", type=("build", "run"))
	depends_on("r-tibble@1.4:", type=("build", "run"))
