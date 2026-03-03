# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidydatatutor(RPackage):
	"""Send Your R Code to 'Tidy Data Tutor'

	Visualize your 'Tidyverse' data analysis pipelines via the 
    'Tidy Data Tutor'(<https://tidydatatutor.com/>) web application.
	"""
	
	homepage = "https://github.com/seankross/tidydatatutor"
	cran = "tidydatatutor" 

	version("0.1.0", md5="f34b103b6fc24bbbbcd53d6f93b26869")

	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
