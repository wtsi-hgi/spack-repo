# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRage(RPackage):
	"""Life History Metrics from Matrix Population Models

	Functions for calculating life history metrics using matrix
    population models ('MPMs'). Described in Jones et al. (2021)
    <doi:10.1101/2021.04.26.441330>.
	"""
	
	homepage = "https://github.com/jonesor/Rage"
	cran = "Rage" 

	version("1.6.0", md5="808709455e295f5cd3af3fb18677d4dc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-popdemo", type=("build", "run"))
