# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrvalidator(RPackage):
	"""Process Control and Validation of Forensic STR Kits

	An open source platform for validation and process control.
    Tools to analyze data from internal validation of forensic short tandem
    repeat (STR) kits are provided. The tools are developed to provide
    the necessary data to conform with guidelines for internal validation
    issued by the European Network of Forensic Science Institutes (ENFSI)
    DNA Working Group, and the Scientific Working Group on DNA Analysis Methods
    (SWGDAM). A front-end graphical user interface is provided.
    More information about each function can be found in the
    respective help documentation.
	"""
	
	homepage = "https://sites.google.com/site/forensicapps/strvalidator"
	cran = "strvalidator" 

	version("2.4.1", md5="a7bbf055dde5d340141c360730d6064d")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-gwidgets2", type=("build", "run"))
	depends_on("r-gwidgets2tcltk@1.0.6:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
