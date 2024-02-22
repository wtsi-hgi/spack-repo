# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContrast(RPackage):
	"""A Collection of Contrast Methods

	One degree of freedom contrasts for 'lm', 'glm', 'gls', and 'geese' objects.
	"""
	
	homepage = "https://github.com/Alanocallaghan/contrast"
	cran = "contrast" 

	version("0.24.2", md5="1e15c3c4490c00466a56afbad6ca3a2d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
