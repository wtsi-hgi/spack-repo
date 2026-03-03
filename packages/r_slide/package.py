# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlide(RPackage):
	"""Single Cell Linkage by Distance Estimation is SLIDE

	This statistical method uses the nearest neighbor algorithm to estimate absolute distances between single cells 
	based on a chosen constellation of surface proteins, with these distances being a measure of the similarity between the 
	two cells being compared. Based on Sen, N., Mukherjee, G., and Arvin, A.M. (2015) <DOI:10.1016/j.ymeth.2015.07.008>.
	"""
	
	cran = "SLIDE" 

	version("1.0.0", md5="16a2c3c67c7f24a1ce79adb28ab1fdeb")

	depends_on("r@3.4:", type=("build", "run"))
