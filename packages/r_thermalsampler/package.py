# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThermalsampler(RPackage):
	"""Calculate Sample Sizes Required for Critical Thermal Limits
Experiments

	We present a range of simulations to aid researchers in determining appropriate sample sizes when performing critical
    thermal limits studies (e.g. CTmin/CTmin experiments). A number of wrapper functions are provided for plotting and summarising outputs
    from these simulations. This package is presented in van Steenderen, C.J.M., Sutton, G.F., Owen, C.A., Martin, G.D., and Coetzee, J.A. Sample size assessments for thermal physiology studies: An R
    package and R Shiny application. 2023. Physiological Entomology. <doi:10.1111/phen.12416>. The GUI version of this package is available on the R Shiny online server at: 
    <https://clarkevansteenderen.shinyapps.io/ThermalSampleR_Shiny/> , or it is accessible via GitHub at <https://github.com/clarkevansteenderen/ThermalSampleR_Shiny/>. We would like
    to thank Grant Duffy (University of Otago, Dundedin, New Zealand) for granting us permission to use the source code for the Test of Total Equivalency function.
	"""
	
	cran = "ThermalSampleR" 

	version("0.1.2", md5="67b765a41bcf223f115cb0b497e52d58")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
