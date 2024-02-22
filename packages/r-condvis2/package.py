# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondvis2(RPackage):
	"""Interactive Conditional Visualization for Supervised and
Unsupervised Models in Shiny

	Constructs a shiny app function with interactive displays for conditional visualization of models, 
     data and density functions. An extended version of package 'condvis'. 
    Catherine B. Hurley, Mark O'Connell,Katarina Domijan (2021) <doi:10.1080/10618600.2021.1983439>. 
	"""
	
	homepage = "https://cbhurley.github.io/condvis2/"
	cran = "condvis2" 

	version("0.1.2", md5="38a7da01d55eb459d2eef337c26fd721", url="https://cran.r-project.org/src/contrib/condvis2_0.1.2.tar.gz")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dendser", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-gower", type=("build", "run"))
