# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDissever(RPackage):
	"""Spatial Downscaling using the Dissever Algorithm

	Spatial downscaling of coarse grid mapping to fine grid
    mapping using predictive covariates and a model fitted using the 'caret'
    package. The original dissever algorithm was published by Malone et al. 
    (2012) <doi:10.1016/j.cageo.2011.08.021>, and extended by Roudier et al.
    (2017) <doi:10.1016/j.compag.2017.08.021>.
	"""
	
	homepage = "https://github.com/pierreroudier/dissever"
	cran = "dissever" 

	version("0.2-3", md5="7413740976980d49c85c9c410591d1b2")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
