# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClarifai(RPackage):
	"""Access to Clarifai API

	Get description of images from Clarifai API. For more information,
    see <http://clarifai.com>. Clarifai uses a large deep learning cloud to come
    up with descriptive labels of the things in an image. It also provides how
    confident it is about each of the labels.
	"""
	
	homepage = "http://github.com/soodoku/clarifai"
	cran = "clarifai" 

	version("0.4.2", md5="2c0b184c54139279f567a174c7531331")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
