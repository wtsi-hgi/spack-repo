# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsearchtools(RPackage):
	"""Binary Search Tools

	Exposes the binary search functions of the C++ standard library (std::lower_bound, std::upper_bound) plus other convenience functions, allowing faster lookups on sorted vectors.
	"""
	
	homepage = "https://github.com/digEmAll/bsearchtools"
	cran = "bsearchtools" 

	version("0.0.61", md5="230426769eb07a133b56cbd0aa3cd8cf")

	depends_on("r-rcpp", type=("build", "run"))
