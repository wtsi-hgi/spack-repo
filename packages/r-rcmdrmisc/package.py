# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrmisc(RPackage):
	"""R Commander Miscellaneous Functions

	
  Various statistical, graphics, and data-management functions used by the Rcmdr package in the R Commander GUI for R.  
	"""
	
	homepage = "https://www.r-project.org"
	cran = "RcmdrMisc" 

	version("2.9-1", md5="2f994765f3455ed94c422f40107906bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car@3.0.0:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-hmisc@4.1.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-readstata13", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
