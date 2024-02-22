# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmisc(RPackage):
	"""Ryan Miscellaneous

	Contains many functions useful for data analysis
    and utility operations.
	"""
	
	cran = "Rmisc" 

	version("1.5.1", md5="9d59ff3e9df9bca3bbfcb6c8832d9014")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
