# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowercomprisk(RPackage):
	"""Power Analysis Tool for Joint Testing Hazards with Competing
Risks Data

	A power analysis tool for jointly testing the cause-1 cause-specific hazard and the any-cause hazard with competing risks data.
	"""
	
	cran = "powerCompRisk" 

	version("1.0.1", md5="19ccba5a6b994a1659eb879dd612e3a9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
