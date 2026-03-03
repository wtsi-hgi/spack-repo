# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsda(RPackage):
	"""Basic Statistics and Data Analysis

	Data sets for book "Basic Statistics and Data Analysis" by
    Larry J. Kitchens.
	"""
	
	homepage = "https://github.com/alanarnholt/BSDA"
	cran = "BSDA" 

	version("1.2.2", md5="64d541438a5b355bc58630270bcfa6ae")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
