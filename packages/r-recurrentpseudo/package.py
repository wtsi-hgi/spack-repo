# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecurrentpseudo(RPackage):
	"""Creates Pseudo-Observations and Analysis for Recurrent Event
Data

	Computation of one-, two- and three-dimensional 
  pseudo-observations based on recurrent events and terminal events. 
  Generalised linear models are fitted using generalised estimating 
  equations. Technical details on the bivariate procedure can be found 
  in "Bivariate pseudo-observations for recurrent event analysis with 
  terminal events" (Furberg et al., 2021) <doi:10.1007/s10985-021-09533-5>. 
	"""
	
	homepage = "https://github.com/JulieKFurberg/recurrentpseudo"
	cran = "recurrentpseudo" 

	version("1.0.0", md5="16bf1e79f9c2dc62f37aa01fff8190fc")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
