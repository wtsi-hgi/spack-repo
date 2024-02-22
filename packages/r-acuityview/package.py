# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcuityview(RPackage):
	"""A Package for Displaying Visual Scenes as They May Appear to an
Animal with Lower Acuity

	This code provides a simple method for representing a visual scene as it may be seen by an animal with less acute vision. When using (or for more information), please cite the original publication.
	"""
	
	cran = "AcuityView" 

	version("0.1", md5="5e518f403d2df0d5f813724fa7e29bb5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-imager@0.40.1:", type=("build", "run"))
	depends_on("r-fftwtools@0.9.7:", type=("build", "run"))
	depends_on("r-plotrix@3.2.3:", type=("build", "run"))
