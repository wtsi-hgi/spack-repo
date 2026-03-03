# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtTest(RPackage):
	"""Robustified t-Test

	Performs one-sample t-test based on robustified statistics using median/MAD (TA) and Hodges-Lehmann/Shamos (TB). For more details, see Park and Wang (2018)<arXiv:1807.02215>. This work was partially supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (No. NRF-2017R1A2B4004169).  
	"""
	
	homepage = "https://github.com/statpnu/R-package"
	cran = "rt.test" 

	version("1.18.7.9", md5="95e78bd69613e1cc72b3463617a546d7")

	depends_on("r@3.2.3:", type=("build", "run"))
