# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFarrell(RPackage):
	"""Interactive Interface to Data Envelopment Analysis Modeling

	Allows the user to execute interactively radial data envelopment analysis models. The user has the ability to upload a data frame, 
    select the input/output variables, choose the technology assumption to adopt and decide whether to run an input or an output oriented model. 
    When the model is executed a set of results are displayed which include efficiency scores, peers' determination, scale efficiencies' evaluation 
    and slacks' calculation. Fore more information about the theoretical background of the package, 
    please refer to Bogetoft & Otto (2011) <doi:10.1007/978-1-4419-7961-2>.
	"""
	
	homepage = "https://github.com/feddelegrand7/farrell"
	cran = "farrell" 

	version("0.2.1", md5="b718b4ea1226163d6a989902b3c24e46")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-benchmarking", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
