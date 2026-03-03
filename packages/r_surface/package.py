# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurface(RPackage):
	"""Fitting Hansen Models to Investigate Convergent Evolution

	This data-driven phylogenetic comparative method fits stabilizing selection models to continuous trait data, building on the 'ouch' methodology of Butler and King (2004) <doi:10.1086/426002>. The main functions fit a series of Hansen models using stepwise AIC, then identify cases of convergent evolution where multiple lineages have shifted to the same adaptive peak. For more information see Ingram and Mahler (2013) <doi:10.1111/2041-210X.12034>.
	"""
	
	homepage = "https://www.otago.ac.nz/ecoevotago/code/surface.html"
	cran = "surface" 

	version("0.5", md5="f511ff85defbe178091231b2d49ed52f")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ouch", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
