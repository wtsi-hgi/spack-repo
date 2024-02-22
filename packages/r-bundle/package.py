# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBundle(RPackage):
	"""Serialize Model Objects with a Consistent Interface

	Typically, models in 'R' exist in memory and can be saved via
    regular 'R' serialization. However, some models store information in
    locations that cannot be saved using 'R' serialization alone. The goal
    of 'bundle' is to provide a common interface to capture this
    information, situate it within a portable object, and restore it for
    use in new settings.
	"""
	
	homepage = "https://github.com/rstudio/bundle"
	cran = "bundle" 

	version("0.1.1", md5="46185da46232808dcd2bb1ec208411e2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
