# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsthmanhanes(RPackage):
	"""Asthma Data Sets from NHANES

	Data sets and examples from National Health and Nutritional Examination Survey (NHANES).
	"""
	
	cran = "AsthmaNHANES" 

	version("1.1.0", md5="6c99b11a1ea000d7b161e28b673deacb")

	depends_on("r@3.5:", type=("build", "run"))
