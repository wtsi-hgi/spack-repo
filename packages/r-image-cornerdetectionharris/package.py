# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageCornerdetectionharris(RPackage):
	"""Implementation of the Harris Corner Detection for Images

	An implementation of the Harris Corner Detection as described in the paper "An Analysis and Implementation of the Harris Corner Detector" by Sánchez J. et al (2018) available at <doi:10.5201/ipol.2018.229>. 
    The package allows to detect relevant points in images which are characteristic to the digital image.
	"""
	
	homepage = "https://github.com/bnosac/image"
	cran = "image.CornerDetectionHarris" 

	version("0.1.2", md5="f9d40fd7f4f370ad35eb967674caa1ab")

	depends_on("r-rcpp", type=("build", "run"))
