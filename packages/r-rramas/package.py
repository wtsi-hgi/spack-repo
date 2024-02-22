# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRramas(RPackage):
	"""Matrix Population Models

	Analyzes and predicts from matrix population models (Caswell 2006) <doi:10.1002/9781118445112.stat07481>.
	"""
	
	cran = "Rramas" 

	version("0.1-6", md5="ff4ec0887a9f6c759b6f867a39879be0")

	depends_on("r-diagram", type=("build", "run"))
