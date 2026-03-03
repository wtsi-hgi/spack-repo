# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHildareadr(RPackage):
	"""Extract Variables from HILDA

	Makes it easy to extract and combine variables from the HILDA (Household, Income and Labour Dynamics in Australia) survey maintained by the Melbourne Institute <https://melbourneinstitute.unimelb.edu.au/hilda>.
	"""
	
	cran = "hildareadR" 

	version("0.2.0", md5="f66ba98c43d991c4dfd459d7f33466de")

	depends_on("r-haven@2.1.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
