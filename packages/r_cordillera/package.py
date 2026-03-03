# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCordillera(RPackage):
	"""Calculation of the OPTICS Cordillera

	Functions for calculating the OPTICS Cordillera. The OPTICS Cordillera measures the amount of 'clusteredness' in a numeric data matrix within a distance-density based framework for a given minimum number of points comprising a cluster, as described in Rusch, Hornik, Mair (2018) <doi:10.1080/10618600.2017.1349664>. There is an R native version with methods for printing, summarizing, and plotting the result. 
	"""
	
	homepage = "https://r-forge.r-project.org/projects/stops/"
	cran = "cordillera" 

	version("1.0-0", md5="011ede9a2149f07fa15543344971d2ba")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
