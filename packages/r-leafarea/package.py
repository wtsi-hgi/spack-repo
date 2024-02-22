# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafarea(RPackage):
	"""Rapid Digital Image Analysis of Leaf Area

	An interface for the image processing program 'ImageJ', which
    allows a rapid digital image analysis for particle sizes. This package includes
    function to write an 'ImageJ' macro which is optimized for a leaf area analysis by
    default.
	"""
	
	homepage = "https://github.com/mattocci27/LeafArea"
	cran = "LeafArea" 

	version("0.1.8", md5="cf0444a09b106a78ec1603a914b7bf6b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("openjdk@1.6.0:", type=("build", "link", "run"))
