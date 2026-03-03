# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfda(RPackage):
	"""Local Fisher Discriminant Analysis

	Functions for performing and visualizing Local Fisher Discriminant
    Analysis(LFDA), Kernel Fisher Discriminant Analysis(KLFDA), and Semi-supervised
    Local Fisher Discriminant Analysis(SELF).
	"""
	
	homepage = "https://github.com/terrytangyuan/lfda"
	cran = "lfda" 

	version("1.1.3", md5="64578ac84157fa108b6262097af8274b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
