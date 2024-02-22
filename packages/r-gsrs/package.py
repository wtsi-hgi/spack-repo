# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsrs(RPackage):
	"""A Group-Specific Recommendation System

	A group-specific recommendation system to use dependency information from users and items which share similar characteristics under the singular value decomposition framework. Refer to paper A Group-Specific Recommender System <doi:10.1080/01621459.2016.1219261> for the details.
	"""
	
	cran = "gsrs" 

	version("0.1.1", md5="84e007314112820cb7892bca2efffad0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
