# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageLibfacedetection(RPackage):
	"""Convolutional Neural Network for Face Detection

	An open source library for face detection in images. 
    Provides a pretrained convolutional neural network based on <https://github.com/ShiqiYu/libfacedetection> which can be used to detect faces which have size greater than 10x10 pixels.
	"""
	
	homepage = "https://github.com/bnosac/image"
	cran = "image.libfacedetection" 

	version("0.1", md5="8069920098365482b139a62b48e76556")

	depends_on("r-rcpp", type=("build", "run"))
