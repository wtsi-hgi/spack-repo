# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpifitter(RPackage):
	"""Analysis and Simulation of Plant Disease Progress Curves

	Analysis and visualization of plant disease progress curve data. Functions for
    fitting two-parameter population dynamics models (exponential, monomolecular, logistic
    and Gompertz) to proportion data for single or multiple epidemics using either linear
    or no-linear regression.  Statistical and visual outputs are provided to aid in model
    selection. Synthetic curves can be simulated for any of the models given the parameters.
    See Laurence V. Madden, Gareth Hughes, and Frank van den Bosch (2007) <doi:10.1094/9780890545058>
    for further information on the methods.
	"""
	
	homepage = "https://github.com/AlvesKS/epifitter"
	cran = "epifitter" 

	version("0.3.0", md5="17b95e3f85567aeb8df3b384709531f2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
