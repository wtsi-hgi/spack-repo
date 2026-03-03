# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoped(RPackage):
	"""Population (and Individual) Optimal Experimental Design

	Optimal experimental designs for both population and individual
    studies based on nonlinear mixed-effect models. Often this is based on a
    computation of the Fisher Information Matrix. This package was developed
    for pharmacometric problems, and examples and predefined models are available
    for these types of systems. The methods are described in Nyberg et al. 
    (2012) <doi:10.1016/j.cmpb.2012.05.005>, and Foracchia et al. (2004) 
    <doi:10.1016/S0169-2607(03)00073-7>.
	"""
	
	homepage = "https://andrewhooker.github.io/PopED/"
	cran = "PopED" 

	version("0.6.0", md5="30d34cb53eb5f4fba4286ac3e1c0bbf0")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
