# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcnet(RPackage):
	"""Optimal Channel Networks

	Generate and analyze Optimal Channel Networks (OCNs): 
	oriented spanning trees reproducing all scaling features characteristic 
	of real, natural river networks. As such, they can be used in a variety 
	of numerical experiments in the fields of hydrology, ecology and 
	epidemiology. See Carraro et al. (2020) <doi:10.1002/ece3.6479> 
	for a presentation of the package; Rinaldo et al. (2014) 
	<doi:10.1073/pnas.1322700111> for a theoretical overview on the OCN 
	concept; Furrer and Sain (2010) <doi:10.18637/jss.v036.i10> for the 
	construct used.
	"""
	
	homepage = "https://lucarraro.github.io/OCNet/"
	cran = "OCNet" 

	version("1.2.1", md5="7ba0790786f268cb881f10f2d68dad02")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-adespatial", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
