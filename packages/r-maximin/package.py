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

	version("1.0-5", md5="ed3f4f9fc96c65599e2986e486f7f6e8")
	version("1.0-4", md5="6ac0f06e7d1441b175a91a7780fa906e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-plgp", type=("build", "run"))
