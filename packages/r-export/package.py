# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExport(RPackage):
	"""Streamlined Export of Graphs and Data Tables

	Easily export 'R' graphs and statistical output to 'Microsoft
    Office' / 'LibreOffice', 'Latex' and 'HTML' Documents, using sensible defaults
    that result in publication-quality output with simple, straightforward commands.
    Output to 'Microsoft Office' is in editable 'DrawingML' vector format for
    graphs, and can use corporate template documents for styling. This enables
    the production of standardized reports and also allows for manual tidy-up
    of the layout of 'R' graphs in 'Powerpoint' before final publication. Export
    of graphs is flexible, and functions enable the currently showing R graph
    or the currently showing 'R' stats object to be exported, but also allow the
    graphical or tabular output to be passed as objects. The package relies on package
    'officer' for export to 'Office' documents,and output files are also fully compatible
    with 'LibreOffice'. Base 'R', 'ggplot2' and 'lattice' plots are supported, as
    well as a wide variety of 'R' stats objects, via wrappers to xtable(), broom::tidy() 
    and stargazer(), including aov(), lm(), glm(), lme(), glmnet() and coxph() as
    well as matrices and data frames and many more...
	"""
	
	cran = "export" 

	version("0.3.0", md5="fe64d329db686477857af38ff1706d28")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-officer@0.2.2:", type=("build", "run"))
	depends_on("r-rvg@0.1.8:", type=("build", "run"))
	depends_on("r-xtable@1.8.2:", type=("build", "run"))
	depends_on("r-flextable@0.4.3:", type=("build", "run"))
	depends_on("r-rgl@0.99.16:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-stargazer@5.2.1:", type=("build", "run"))
	depends_on("r-openxlsx@4.0.17:", type=("build", "run"))
	depends_on("r-broom@0.4.4:", type=("build", "run"))
	depends_on("r-devemf@3.8:", type=("build", "run"))
