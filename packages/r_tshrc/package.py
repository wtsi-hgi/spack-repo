# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTshrc(RPackage):
	"""Two Stage Hazard Rate Comparison

	Two-stage procedure compares hazard rate functions,
    which may or may not cross each other.
	"""
	
	cran = "TSHRC" 

	version("0.1-6", md5="71e22850fb9fded8d4186a62b606a7c7")

	depends_on("r@3.0.2:", type=("build", "run"))
