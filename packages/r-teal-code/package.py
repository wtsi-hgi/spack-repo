# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealCode(RPackage):
	"""Code Storage and Execution Class for 'teal' Applications

	Introduction of 'qenv' S4 class, that facilitates code
    execution and reproducibility in 'teal' applications.
	"""
	
	homepage = "https://insightsengineering.github.io/teal.code/"
	cran = "teal.code" 

	version("0.5.0", md5="8ab7f3254af379f3037036f12fdc2661")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
