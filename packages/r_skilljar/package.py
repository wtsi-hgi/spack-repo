# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkilljar(RPackage):
	"""Connect to Your 'Skilljar' Data

	Functions that simplify calls to the 'Skilljar' API. See 
    <https://api.skilljar.com/docs/> for documentation on the 'Skilljar' API.
    This package is not supported by 'Skilljar'.
	"""
	
	cran = "skilljaR" 

	version("0.1.2", md5="780de86f5207b8341e8edbc9a9f1505e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
