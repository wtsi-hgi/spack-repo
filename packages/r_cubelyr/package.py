# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCubelyr(RPackage):
	"""A Data Cube 'dplyr' Backend

	An implementation of a data cube extracted out of 'dplyr' for
    backward compatibility.
	"""
	
	homepage = "https://github.com/hadley/cubelyr"
	cran = "cubelyr" 

	version("1.0.2", md5="18a51db2bee1d3dd92a64f9ac16b84cc")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
