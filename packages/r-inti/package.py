# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInti(RPackage):
	"""Tools and Statistical Procedures in Plant Science

	The 'inti' package is part of the 'inkaverse' project for developing 
    different procedures and tools used in plant science and experimental designs. 
    The mean aim of the package is to support researchers during the planning of
    experiments and data collection (tarpuy()), data analysis and graphics (yupana())
    , and technical writing. 
    Learn more about the 'inkaverse' project at <https://inkaverse.com/>.
	"""
	
	homepage = "https://inkaverse.com/"
	cran = "inti" 

	version("0.6.4", md5="268738d07711ff3c930bb6c651a9e9b3")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
