# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPivottabler(RPackage):
	"""Create Pivot Tables

	Create regular pivot tables with just a few lines of R.  
    More complex pivot tables can also be created, e.g. pivot tables
    with irregular layouts, multiple calculations and/or derived 
    calculations based on multiple data frames.  Pivot tables are
    constructed using R only and can be written to a range of
    output formats (plain text, 'HTML', 'Latex' and 'Excel'), 
    including with styling/formatting.
	"""
	
	homepage = "http://www.pivottabler.org.uk/"
	cran = "pivottabler" 

	version("1.5.5", md5="7bb76f03c40527fccd5ac08ce305b647")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6@2.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-htmltools@0.3.5:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.8:", type=("build", "run"))
