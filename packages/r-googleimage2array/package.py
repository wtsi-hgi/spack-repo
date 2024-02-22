# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoogleimage2array(RPackage):
	"""Create Array Data from 2D Image Thumbnails via Google Image
Search

	Images are provided as an array dataset of 2D image thumbnails from Google Image Search <https://www.google.com/search>.
  This array data may be suitable for a training data of machine learning or deep learning as a first trial.
	"""
	
	homepage = "https://github.com/kumeS/GoogleImage2Array"
	cran = "GoogleImage2Array" 

	version("0.99.2", md5="cc94c4031642e946eb0f42d26fed0e43")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
