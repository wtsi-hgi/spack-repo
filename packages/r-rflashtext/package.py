# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRflashtext(RPackage):
	"""FlashText Algorithm for Finding and Replacing Words

	Implementation of the FlashText algorithm, by Singh (2017) <arXiv:1711.00046>. It can be used to find and replace words in a given text with only one pass over the document.
	"""
	
	homepage = "https://github.com/AbrJA/rflashtext"
	cran = "rflashtext" 

	version("1.0.0", md5="147f25cc2991a0a74208dadd671f9dcf")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
