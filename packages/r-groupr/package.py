# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroupr(RPackage):
	"""Groups with Inapplicable Values

	The 'groupr' package provides a more powerful version of grouped
  tibbles from 'dplyr'. It allows groups to be marked inapplicable,
  which is a simple but widely useful way to express structure in a dataset.
  It also provides powerful pivoting and other group manipulation functions.
	"""
	
	homepage = "https://github.com/ngriffiths21/groupr"
	cran = "groupr" 

	version("0.1.2", md5="e91bce559c15122f967adbf57e20e299")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
