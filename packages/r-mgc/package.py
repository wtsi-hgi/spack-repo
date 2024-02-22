# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgc(RPackage):
	"""Multiscale Graph Correlation

	Multiscale Graph Correlation (MGC) is a framework developed by Vogelstein et al. (2019) <DOI:10.7554/eLife.41690> that extends global correlation procedures to be multiscale; consequently, MGC tests typically require far fewer samples than existing methods for a wide variety of dependence structures and dimensionalities, while maintaining computational efficiency. Moreover, MGC provides a simple and elegant multiscale characterization of the potentially complex latent geometry underlying the relationship.
	"""
	
	homepage = "https://github.com/neurodata/r-mgc"
	cran = "mgc" 

	version("2.0.2", md5="58751629776bca234d2feb00d124fade")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
