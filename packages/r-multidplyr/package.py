# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultidplyr(RPackage):
	"""A Multi-Process 'dplyr' Backend

	Partition a data frame across multiple worker processes to
    provide simple multicore parallelism.
	"""
	
	homepage = "https://multidplyr.tidyverse.org"
	cran = "multidplyr" 

	version("0.1.3", md5="06df032a00e0e74c000d911f644a68ed")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-callr@3.5.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-qs@0.24.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs@0.3.6:", type=("build", "run"))
