# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtendedfamily(RPackage):
	"""Additional Families for Generalized Linear Models

	Creates family objects identical to stats
    family but for new links.
	"""
	
	cran = "extendedFamily" 

	version("0.2.4", md5="305f98bef3aac9cc4bf816e163cc9ce0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
