# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAltcdfenvs(RPackage):
	"""alternative CDF environments (aka probeset mappings).

	Convenience data structures and functions to handle cdfenvs."""

	bioc = "altcdfenvs"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/altcdfenvs_2.64.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/altcdfenvs/altcdfenvs_2.64.0.tar.gz"]

	version("2.64.0", md5="8bd83d29c11857ae73a4046289748f90")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-biocgenerics@0.1:", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-biobase@2.15.1:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-makecdfenv", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-hypergraph", type=("build", "run"))
