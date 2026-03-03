# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheem(RPackage):
	"""Interactively Explore Local Explanations with the Radial Tour

	Given a non-linear model, calculate the local explanation. 
    We purpose view the data space, explanation 
    space, and model residuals as ensemble graphic interactive on a shiny 
    application. After an observation of interest is identified, the normalized 
    variable importance of the local explanation is used as a 1D projection
    basis. The support of the local explanation is then explored by changing
    the basis with the use of the radial tour <doi:10.32614/RJ-2020-027>; 
    <doi:10.1080/10618600.1997.10474754>.
	"""
	
	homepage = "https://github.com/nspyrison/cheem/"
	cran = "cheem" 

	version("0.4.0.0", md5="aac50eb8343dc9482925420ad26c832b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spinifex@0.3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-conflicted", type=("build", "run"))
