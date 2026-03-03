# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExploratory(RPackage):
	"""A Tool for Large-Scale Exploratory Analyses

	Conduct numerous exploratory analyses in an instant with a 
    point-and-click interface. With one simple command, this tool 
    launches a Shiny App on the local machine. Drag and drop variables 
    in a data set to categorize them as possible independent, 
    dependent, moderating, or mediating variables. Then run dozens 
    (or hundreds) of analyses instantly to uncover any statistically 
    significant relationships among variables. Any relationship 
    thus uncovered should be tested in follow-up studies. 
    This tool is designed only to facilitate exploratory 
    analyses and should NEVER be used for p-hacking. Many of 
    the functions used in this package are previous versions of functions
    in the R Packages 'kim' and 'ezr'.
    Selected References:
    Chang et al. (2021) <https://CRAN.R-project.org/package=shiny>.
    Dowle et al. (2021) <https://CRAN.R-project.org/package=data.table>.
    Kim (2023) <https://jinkim.science/docs/kim.pdf>.
    Kim (2021) <doi:10.5281/zenodo.4619237>.
    Kim (2020) <https://CRAN.R-project.org/package=ezr>.
    Simmons et al. (2011) <doi:10.1177/0956797611417632>
    Tingley et al. (2019) <https://CRAN.R-project.org/package=mediation>.
    Wickham et al. (2020) <https://CRAN.R-project.org/package=ggplot2>.
	"""
	
	homepage = "https://exploratoryonly.com"
	cran = "exploratory" 

	version("0.3.31", md5="42116a23c817a208c71171c6a177666f")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-lemon", type=("build", "run"))
	depends_on("r-lm-beta", type=("build", "run"))
	depends_on("r-mediation", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))
