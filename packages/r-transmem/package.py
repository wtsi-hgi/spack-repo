# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransmem(RPackage):
	"""Treatment of Membrane-Transport Data

	Treatment and visualization of membrane (selective) transport 
    data. Transport profiles involving up to three species are produced as
    publication-ready plots and several membrane performance parameters 
    (e.g. separation factors as defined in Koros et al. (1996) 
    <doi:10.1351/pac199668071479> and non-linear regression parameters
    for the equations described in Rodriguez de San Miguel et al. (2014)
    <doi:10.1016/j.jhazmat.2014.03.052>) can be obtained. Many widely used 
    experimental setups (e.g. membrane physical aging) can be easily studied
    through the package's graphical representations. 
	"""
	
	homepage = "https://CRAN.R-project.org/package=transmem"
	cran = "transmem" 

	version("0.1.1", md5="a3ae980466115ace8b9a7d4dbc419690")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cmna", type=("build", "run"))
	depends_on("r-ggformula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
