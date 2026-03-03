# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvd(RPackage):
	"""Color Vision Deficiencies

	Methods for color vision deficiencies (CVD), to help understanding and mitigating issues with CVDs and to generate tests for diagnosis and interpretation.
	"""
	
	cran = "CVD" 

	version("1.0.2", md5="15d447dbbda0bfe5daf60511350de4fe")

	depends_on("r@2.10:", type=("build", "run"))
