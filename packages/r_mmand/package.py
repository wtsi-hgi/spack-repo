# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmand(RPackage):
	"""Mathematical Morphology in Any Number of Dimensions

	Provides tools for performing mathematical morphology operations,
    such as erosion and dilation, on data of arbitrary dimensionality. Can also
    be used for finding connected components, resampling, filtering, smoothing
    and other image processing-style operations.
	"""
	
	homepage = "https://github.com/jonclayden/mmand"
	cran = "mmand" 

	version("1.6.3", md5="9716940ae9f4a9e9ad3a8c4e889728a7")

	depends_on("r-rcpp", type=("build", "run"))
