# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultimode(RPackage):
	"""Mode Testing and Exploring

	Different examples and methods for testing (including different proposals described in Ameijeiras-Alonso et al., 2019 <DOI:10.1007/s11749-018-0611-5>) and exploring (including the mode tree, mode forest and SiZer) the number of modes using nonparametric techniques <DOI:10.18637/jss.v097.i09>.
	"""
	
	homepage = "https://doi.org/10.18637/jss.v097.i09"
	cran = "multimode" 

	version("1.5", md5="7732a367571085e318aea8be8216218b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
