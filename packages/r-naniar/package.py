# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaniar(RPackage):
	"""Data Structures, Summaries, and Visualisations for Missing Data

	Missing values are ubiquitous in data and need to be explored and
    handled in the initial stages of analysis. 'naniar' provides data 
    structures and functions that facilitate the plotting of missing values and 
    examination of imputations. This allows missing data dependencies to be 
    explored with minimal deviation from the common work patterns of 'ggplot2' 
    and tidy data. The work is fully discussed at Tierney & Cook (2023) 
    <doi:10.18637/jss.v105.i07>.
	"""
	
	homepage = "https://github.com/njtierney/naniar"
	cran = "naniar" 

	version("1.0.0", md5="643a9121342f5bfd9b8cade850c6b5cd")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-visdat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
