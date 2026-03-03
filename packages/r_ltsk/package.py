# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtsk(RPackage):
	"""Local Time Space Kriging

	Implements local spatial and local spatiotemporal Kriging based on local spatial and local spatiotemporal variograms, respectively. The method is documented in Kumar et al (2013) <https://www.nature.com/articles/jes201352)>.
	"""
	
	cran = "ltsk" 

	version("1.1.1", md5="595924fa843768110832dd7e73eb6a4e")

	depends_on("r@2.10:", type=("build", "run"))
