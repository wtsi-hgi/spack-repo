# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForesthes(RPackage):
	"""Forest Health Evaluation System at the Forest Stand Level in
China

	Assessing forest ecosystem health is an effective way for forest
    resource management.The national forest health evaluation system at the forest 
    stand level using analytic hierarchy process, has a high application value 
    and practical significance. The package can effectively and easily realize the 
    total assessment process, and help foresters to further assess and management 
    forest resources.
	"""
	
	cran = "forestHES" 

	version("1.0-1", md5="88ea839d450fba27e9dc44c0264a952f")

	depends_on("r@3.4:", type=("build", "run"))
