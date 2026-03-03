# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeach(RPackage):
	"""Biometric Exploratory Analysis Creation House

	A platform is provided for interactive analyses with a goal of totally easy to develop, deploy, interact, and explore (TEDDIE). Using this package, users can create customized analyses and make them available to end users who can perform interactive analyses and save analyses to RTF or HTML files. It allows developers to focus on R code for analysis, instead of dealing with html or shiny code.
	"""
	
	homepage = "https://www.pharmasug.org/proceedings/2018/AD/PharmaSUG-2018-AD05.pdf"
	cran = "BEACH" 

	version("1.3.1", md5="d17447a7916cb0f3cbf3ce206f472bc7")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-shiny@0.12.2:", type=("build", "run"))
	depends_on("r-dt@0.1:", type=("build", "run"))
	depends_on("r-haven@0.1.1:", type=("build", "run"))
	depends_on("r-xtable@1.7.4:", type=("build", "run"))
	depends_on("r-rtf@0.4.11:", type=("build", "run"))
	depends_on("r-plyr@1.8.2:", type=("build", "run"))
	depends_on("r-sas7bdat@0.5:", type=("build", "run"))
	depends_on("r-writexls@3.5.1:", type=("build", "run"))
	depends_on("r-rjava@0.9.6:", type=("build", "run"))
	depends_on("r-devtools@1.9:", type=("build", "run"))
