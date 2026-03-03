# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJnplots(RPackage):
	"""Visualize Outputs from the 'Johnson-Neyman' Technique

	Aids in the calculation and visualization of regions of non-significance using the 'Johnson-Neyman' technique and its extensions as described by Bauer and Curran (2005) <doi:10.1207/s15327906mbr4003_5> to assess the influence of categorical and continuous moderators. Allows correcting for phylogenetic relatedness.
	"""
	
	homepage = "https://github.com/kenstoyama/JNplots"
	cran = "JNplots" 

	version("0.1.1", md5="de20b6573a9643fc65b3b0550b9368d6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
