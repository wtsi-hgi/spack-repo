# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDimred(RPackage):
	"""A Framework for Dimensionality Reduction

	A collection of dimensionality reduction
    techniques from R packages and a common
    interface for calling the methods.
	"""
	
	homepage = "https://www.guido-kraemer.com/software/dimred/"
	cran = "dimRed" 

	version("0.2.6", md5="1cef3b06c7f0eea422fedbbf04a28e63")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-drr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
