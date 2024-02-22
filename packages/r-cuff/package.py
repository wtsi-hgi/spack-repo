# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuff(RPackage):
	"""Charles's Utility Function using Formula

	Utility functions that provides wrapper to descriptive base functions
  like cor, mean and table.  It makes use of the formula interface to pass
  variables to functions.  It also provides operators to concatenate (%+%), to
  repeat (%n%) and manage character vectors for nice display.
	"""
	
	homepage = "https://github.com/giguerch/CUFF"
	cran = "CUFF" 

	version("1.9", md5="3896a0cddcb851b7423a6e323d1eec45")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
