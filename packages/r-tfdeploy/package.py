# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfdeploy(RPackage):
	"""Deploy 'TensorFlow' Models

	Tools to deploy 'TensorFlow' <https://www.tensorflow.org/> models across 
  multiple services. Currently, it provides a local server for testing 'cloudml' 
  compatible services.
	"""
	
	cran = "tfdeploy" 

	version("0.6.1", md5="6877bb39294db28a338c4f07293ff9c8")

	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-swagger", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
