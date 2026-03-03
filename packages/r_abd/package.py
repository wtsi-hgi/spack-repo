# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbd(RPackage):
	"""The Analysis of Biological Data

	The abd package contains data sets and sample code for The
    Analysis of Biological Data by Michael Whitlock and Dolph Schluter (2009;
    Roberts & Company Publishers).
	"""
	
	cran = "abd" 

	version("0.2-8", md5="1913d76a0fbc44222709381f63f385b9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mosaic", type=("build", "run"))
