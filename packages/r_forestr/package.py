# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestr(RPackage):
	"""Ecosystem and Canopy Structural Complexity Metrics from LiDAR

	Provides a toolkit for calculating forest and canopy structural complexity metrics from
    terrestrial LiDAR (light detection and ranging). References:  Atkins et al. 2018 <doi:10.1111/2041-210X.13061>; Hardiman et al. 2013 <doi:10.3390/f4030537>;
    Parker et al. 2004 <doi:10.1111/j.0021-8901.2004.00925.x>.
	"""
	
	homepage = "https://github.com/atkinsjeff/forestr"
	cran = "forestr" 

	version("2.0.2", md5="3fdc9c0a3463eab6b05bb9550ef399d4")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
