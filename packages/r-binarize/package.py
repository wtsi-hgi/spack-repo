# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinarize(RPackage):
	"""Binarization of One-Dimensional Data

	Provides methods for the binarization of one-dimensional data and some visualization functions.
	"""
	
	cran = "Binarize" 

	version("1.3.1", md5="a8b5fd250b361e6e7eb452651da926fa")

	depends_on("r-diptest", type=("build", "run"))
