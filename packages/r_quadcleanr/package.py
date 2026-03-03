# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuadcleanr(RPackage):
	"""Cleanup and Visualization of Quadrat Data

	A tool that can be customized to aid in the clean up of ecological data 
    collected using quadrats and can crop quadrats to ensure comparability between
    quadrats collected under different methodologies.
	"""
	
	homepage = "https://github.com/DominiqueMaucieri/quadcleanR"
	cran = "quadcleanR" 

	version("1.1.0", md5="a2bd6cef522090e6535461c1309dd00f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
