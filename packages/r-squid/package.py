# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSquid(RPackage):
	"""Statistical Quantification of Individual Differences

	A simulation-based tool made to help researchers to become familiar with
    multilevel variations, and to build up sampling designs for their study. 
    This tool has two main objectives: First, it provides an educational tool useful for students, 
    teachers and researchers who want to learn to use mixed-effects models. 
    Users can experience how the mixed-effects model framework can be used to understand 
    distinct biological phenomena by interactively exploring simulated multilevel data. 
    Second, it offers research opportunities to those who are already familiar with 
    mixed-effects models, as it enables the generation of data sets that users may download 
    and use for a range of simulation-based statistical analyses such as power 
    and sensitivity analysis of multilevel and multivariate data [Allegue, H., Araya-Ajoy, Y.G., Dingemanse, 
    N.J., Dochtermann N.A., Garamszegi, L.Z., Nakagawa, S., Reale, D., Schielzeth, H. and Westneat, D.F. (2016) 
    <doi: 10.1111/2041-210X.12659>].
	"""
	
	homepage = "https://github.com/squid-group/squid"
	cran = "squid" 

	version("0.2.1", md5="602194177b0d46665e95212724260511")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinymatrix@0.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-plotly@4.9.3:", type=("build", "run"))
	depends_on("r-mass@7.3.53.1:", type=("build", "run"))
	depends_on("r-lme4@1.1.21:", type=("build", "run"))
	depends_on("r-arm@1.10.1:", type=("build", "run"))
	depends_on("r-data-table@1.1.27.1:", type=("build", "run"))
	depends_on("r-brms@2.15:", type=("build", "run"))
