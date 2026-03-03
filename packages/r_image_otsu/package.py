# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageOtsu(RPackage):
	"""Otsu's Image Segmentation Method

	An implementation of the Otsu's Image Segmentation Method described in the paper: "A C++ Implementation of Otsu's Image Segmentation Method". The algorithm is explained at <doi:10.5201/ipol.2016.158>.
	"""
	
	homepage = "https://github.com/bnosac/image"
	cran = "image.Otsu" 

	version("0.1", md5="a6fb8f3ed114981f2ebbd7b399d03941")

	depends_on("r-rcpp", type=("build", "run"))
