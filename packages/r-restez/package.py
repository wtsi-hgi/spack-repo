# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestez(RPackage):
	"""Create and Query a Local Copy of 'GenBank' in R

	Download large sections of
    'GenBank' <https://www.ncbi.nlm.nih.gov/genbank/> and generate a local
    SQL-based database. A user can then query this database using 'restez'
    functions or through 'rentrez' <https://CRAN.R-project.org/package=rentrez>
    wrappers.
	"""
	
	homepage = "https://github.com/ropensci/restez"
	cran = "restez" 

	version("2.1.4", md5="45c687ff6e41c0462f7af0323cec13e0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-duckdb", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
