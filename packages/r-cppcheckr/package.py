# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCppcheckr(RPackage):
	"""Check 'C' and 'C++' Files using 'Cppcheck'

	Allow to run 'Cppcheck' (<https://cppcheck.sourceforge.io/>)
    on 'C' and 'C++' files with a 'R' command or a 'RStudio' addin. The report
    appears in the 'RStudio' viewer pane as a formatted 'HTML' file. It is
    also possible to get this report with a 'shiny' application. 'Cppcheck' 
    can spot many error types and it can also give some recommendations on the 
    code.
	"""
	
	homepage = "https://github.com/stla/cppcheckR"
	cran = "cppcheckR" 

	version("1.0.0", md5="4cf8d17b7b559b2dd820b6edb066faed")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("cppcheck", type=("build", "link", "run"))
