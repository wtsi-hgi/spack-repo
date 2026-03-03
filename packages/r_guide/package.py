# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuide(RPackage):
	"""GUI for DErivatives in R

	A nice GUI for financial DErivatives in R.
	"""
	
	cran = "GUIDE" 

	version("1.2.7", md5="19d7166be0da51af911de5e7ca56fd40")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rpanel", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
