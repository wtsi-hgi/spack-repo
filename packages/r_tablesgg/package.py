# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTablesgg(RPackage):
	"""Presentation-Quality Tables, Displayed Using 'ggplot2'

	Presentation-quality tables are displayed as plots on an R 
  graphics device.  Although there are other packages that format tables 
  for display, this package is unique in combining two features: (a) It is 
  aware of the logical structure of the table being presented, and makes 
  use of that for automatic layout and styling of the table.  This avoids 
  the need for most manual adjustments to achieve an attractive result. 
  (b) It displays tables using 'ggplot2' graphics.  Therefore a table can 
  be presented anywhere a graph could be, with no more effort.  External 
  software such as LaTeX or HTML or their viewers is not required.  The 
  package provides a full set of tools to control the style and appearance 
  of tables, including titles, footnotes and reference marks, horizontal 
  and vertical rules, and spacing of rows and columns.  Methods are included 
  to display matrices; data frames; tables created by R's ftable(), table(), 
  and xtabs() functions; and tables created by the 'tables' and 'xtable' 
  packages.  Methods can be added to display other table-like objects.  A 
  vignette is included that illustrates usage and options available in the 
  package.
	"""
	
	homepage = "https://github.com/rrprf/tablesgg"
	cran = "tablesgg" 

	version("0.9-1", md5="0739e76964c0fb3340fbc6fa60b22247")

	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-tables", type=("build", "run"))
