# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDhh(RPackage):
	"""A Heavy-Headed Distribution

	The density, cumulative distribution, quantiles, 
    and i.i.d random variables of a heavy-headed distribution.
    For more information, please see the vignette.
	"""
	
	cran = "dhh" 

	version("0.0.1", md5="c57417523bece5eb4814ab66280eb970")

	depends_on("r@3.5:", type=("build", "run"))
