# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZooid(RPackage):
	"""Load, Segment and Classify Zooplankton Images

	This tool provides functions to load, segment and classify zooplankton images. 
  The image processing algorithms and the machine learning classifiers in this package are (will be, since these have not been added yet) direct ports of 
  an early 'python' implementation that can be found at <https://github.com/arickGrootveld/ZooID>. The model weights and datasets (also not added yet) 
  that are a part of this package can also be found at Arick Grootveld, Eva R. Kozak, Carmen Franco-Gordo (2023) <doi:10.5281/zenodo.7979996>. 
	"""
	
	homepage = "https://github.com/arickGrootveld/ZooID_RPackage"
	cran = "ZooID" 

	version("0.2.0", md5="8a20bcdb7ecfdca12251cd0d7f9f9a1e")

	depends_on("r-magick", type=("build", "run"))
