# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrendadb(RPackage):
	"""The BRENDA Enzyme Database

	R interface for importing and analyzing enzyme information from the BRENDA database.
	"""
	
	homepage = "https://github.com/y1zhou/brendaDb"
	bioc = "brendaDb"

	version("1.22.0", commit="3aab39b2bc47c101b80dd7b626d795d833778aa4")
	version("1.16.0", commit="b1861ff58a4601d5806fd5f0af950caa688c7aa8")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
