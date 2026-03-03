# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBitrina(RPackage):
	"""Binarization and Trinarization of One-Dimensional Data

	Provides methods for the binarization and trinarization of one-dimensional data and some visualization functions.
	"""
	
	cran = "BiTrinA" 

	version("1.3.1", md5="1d91145f7ffd37dc4e3d16d0dccf6372")

	depends_on("r-diptest", type=("build", "run"))
