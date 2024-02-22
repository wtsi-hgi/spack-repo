# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaximin(RPackage):
	"""Space-Filling Design under Maximin Distance

	Constructs a space-filling design under the criterion of maximum-minimum distance. Both discrete and continuous searches are provided.
	"""
	
	cran = "maximin" 

	version("1.0-4", md5="6ac0f06e7d1441b175a91a7780fa906e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plgp", type=("build", "run"))
