# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageDlib(RPackage):
	"""Image Processing Functionality using the 'dlib' Package

	Facility wrappers around the image processing functionality of
    'dlib'. 'Dlib' <http://dlib.net> is a 'C++' toolkit containing machine learning
    algorithms and computer vision tools. Currently the package allows to find feature
    descriptors of digital images, in particular 'SURF' and 'HOG' descriptors.
	"""
	
	homepage = "https://github.com/bnosac/image"
	cran = "image.dlib" 

	version("0.1.1", md5="04de18c3eb1db7a2f400710d4f2cc174")

	depends_on("r-rcpp", type=("build", "run"))
