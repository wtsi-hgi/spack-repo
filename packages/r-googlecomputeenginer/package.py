# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGooglecomputeenginer(RPackage):
	"""R Interface with Google Compute Engine

	Interact with the 'Google Compute Engine' API in R. Lets you create, 
  start and stop instances in the 'Google Cloud'.  Support for preconfigured instances, 
  with templates for common R needs. 
	"""
	
	homepage = "https://cloudyr.github.io/googleComputeEngineR/"
	cran = "googleComputeEngineR" 

	version("0.3.0", md5="986a44ea12eccacfaa162e8fd992257f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-future@1.2:", type=("build", "run"))
	depends_on("r-googleauthr@0.7:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.1:", type=("build", "run"))
