# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidytidbits(RPackage):
	"""A Collection of Tools and Helpers Extending the Tidyverse

	A selection of various tools to extend a data analysis workflow based on the 'tidyverse' packages.
  This includes high-level data frame editing methods (in the style of 'mutate'/'mutate_at'), some methods in the style of
  'purrr' and 'forcats', 'lookup' methods for dict-like lists, a generic method for lumping a data frame by a given count,
  various low-level methods for special treatment of 'NA' values, 'python'-style tuple-assignment and 'truthy'/'falsy' checks,
  saving to PDF and PNG from a pipe and various small utilities.
	"""
	
	cran = "tidytidbits" 

	version("0.3.2", md5="cbd8c8322dc876362df7b9c5d1f6d409")

	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
