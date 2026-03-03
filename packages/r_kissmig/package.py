# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKissmig(RPackage):
	"""a Keep It Simple Species Migration Model

	Simulating species migration and range dynamics under stable or changing environmental conditions based on a simple, raster-based, stochastic migration model. Providing accessibility from an origin or previous distribution for niche-based species distribution models. Nobis & Normand (2014) <doi:10.1111/ecog.00930>.
	"""
	
	homepage = "https://purl.oclc.org/wsl/kissmig"
	cran = "kissmig" 

	version("1.0-4", md5="e07c8a1d1e03d61a7cf22edea5e0ff17")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
