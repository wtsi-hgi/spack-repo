# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlextable(RPackage):
	"""Functions for Tabular Reporting

	Use a grammar for creating and customizing pretty tables. 
 The following formats are supported: 'HTML', 'PDF', 'RTF', 
 'Microsoft Word', 'Microsoft PowerPoint' and R 'Grid Graphics'. 
 'R Markdown', 'Quarto' and the package 'officer' can be used to produce 
 the result files. The syntax is the same for the user regardless of 
 the type of output to be produced. A set of functions allows the 
 creation, definition of cell arrangement, addition of headers or 
 footers, formatting and definition of cell content with text and 
 or images. The package also offers a set of high-level functions 
 that allow tabular reporting of statistical models and the 
 creation of complex cross tabulations.
	"""
	
	homepage = "https://ardata-fr.github.io/flextable-book/"
	cran = "flextable" 

	version("0.9.5", md5="6c2d389406b40e88f4f01e32f9af2ca9")
	version("0.9.4", md5="6136f0e007856ed030bc6f537e15aa4b")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ragg", type=("build", "run"))
	depends_on("r-officer@0.6.5:", type=("build", "run"))
	depends_on("r-gdtools@0.3.6:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-uuid@0.1.4:", type=("build", "run"))
