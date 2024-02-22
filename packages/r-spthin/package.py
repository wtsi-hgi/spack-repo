# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpthin(RPackage):
	"""Functions for Spatial Thinning of Species Occurrence Records for
Use in Ecological Models

	A set of functions that can be used to spatially thin
    species occurrence data. The resulting thinned data can be used in ecological
    modeling, such as ecological niche modeling.
	"""
	
	cran = "spThin" 

	version("0.2.0", md5="5d51aefe4ef92bee343840b26684efff")

	depends_on("r-spam", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
