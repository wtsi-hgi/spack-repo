# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfcentral(RPackage):
	"""Spatial Centrality and Dispersion Statistics

	Computing centrographic statistics (central points, standard 
    distance, standard deviation ellipse, standard deviation box) for 
    observations taken at point locations in 2D or 3D. The 'sfcentral' library 
    was inspired in 'aspace' package but conceived to be used in a spatial
    'tidyverse' context.
	"""
	
	homepage = "https://gavg712.gitlab.io/sfcentral/"
	cran = "sfcentral" 

	version("0.1.0", md5="694c0ae6def4b8fafed5acb56a3c1b30")

	depends_on("r-geodist@0.0.7:", type=("build", "run"))
	depends_on("r-hmisc@4.6:", type=("build", "run"))
	depends_on("r-lwgeom@0.2:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-sf@1.0.8:", type=("build", "run"))
