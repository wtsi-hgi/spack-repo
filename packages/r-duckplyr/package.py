# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDuckplyr(RPackage):
	"""A 'DuckDB'-Backed Version of 'dplyr'

	A drop-in replacement for 'dplyr', powered by 'DuckDB' for performance.
    Also defines a set of generics that provide a low-level
    implementer's interface for the high-level user interface of 'dplyr'.
	"""
	
	homepage = "https://duckdblabs.github.io/duckplyr/"
	cran = "duckplyr" 

	version("0.3.1", md5="0e847941bfed8dfab72d8a5497656860")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-collections", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-duckdb@0.9.1.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs@0.6.3:", type=("build", "run"))
