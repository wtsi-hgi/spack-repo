# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeepack(RPackage):
	"""Generalized Estimating Equation Package

	Generalized estimating equations solver for parameters in
    mean, scale, and correlation structures, through mean link,
    scale link, and correlation link. Can also handle clustered
    categorical responses. See e.g. Halekoh and Højsgaard, (2005,
    <doi:10.18637/jss.v015.i02>), for details. 
	"""
	
	cran = "geepack" 

	version("1.3.10", md5="0d510db65fc726eb4e4085a2340c1629")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
