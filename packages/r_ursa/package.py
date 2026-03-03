# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUrsa(RPackage):
	"""Non-Interactive Spatial Tools for Raster Processing and
Visualization

	S3 classes and methods for manipulation with georeferenced raster data: reading/writing, processing, multi-panel visualization.
	"""
	
	homepage = "https://github.com/nplatonov/ursa"
	cran = "ursa" 

	version("3.10.4", md5="d6f846368e965c1ada02d66adf86fa09")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-sf@0.6.1:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
