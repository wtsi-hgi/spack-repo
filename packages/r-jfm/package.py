# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJfm(RPackage):
	"""Rock Mass Structural Analysis from 3D Mesh of Point Cloud

	Provides functions to extract joint planes from 3D triangular mesh derived
             from point cloud and makes data available for structural analysis.
	"""
	
	cran = "JFM" 

	version("1.0", md5="c226dd0a660971bca6e20d1d8fc3103d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass@7.3.50:", type=("build", "run"))
	depends_on("r-rgl@0.99.16:", type=("build", "run"))
	depends_on("r-rockfab@1.2:", type=("build", "run"))
	depends_on("r-rvcg@0.17:", type=("build", "run"))
	depends_on("r-randomcolor@1.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
