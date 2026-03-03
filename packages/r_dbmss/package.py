# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbmss(RPackage):
	"""Distance-Based Measures of Spatial Structures

	Simple computation of spatial statistic functions of distance to characterize the spatial structures of mapped objects, following Marcon, Traissac, Puech, and Lang (2015) <doi:10.18637/jss.v067.c03>.
  Includes classical functions (Ripley's K and others) and more recent ones used by spatial economists (Duranton and Overman's Kd, Marcon and Puech's M). 
  Relies on 'spatstat' for some core calculation.
	"""
	
	homepage = "https://github.com/EricMarcon/dbmss"
	cran = "dbmss" 

	version("2.9-0", md5="1c32d3fba07fa01608e20c038cbd4256")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-spatstat-utils", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
