# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpss(RPackage):
	"""Tables, Labels and Some Useful Functions from Spreadsheets and
'SPSS' Statistics

	Package computes and displays tables with support for 'SPSS'-style 
        labels, multiple and nested banners, weights, multiple-response variables 
        and significance testing. There are facilities for nice output of tables 
        in 'knitr', 'Shiny', '*.xlsx' files, R and 'Jupyter' notebooks. Methods 
        for labelled variables add value labels support to base R functions and to 
        some functions from other packages. Additionally, the package brings 
        popular data transformation functions from 'SPSS' Statistics and 'Excel': 
        'RECODE', 'COUNT', 'COUNTIF', 'VLOOKUP' and etc. 
        These functions are very useful for data processing in marketing research 
        surveys. Package intended to help people to move data 
        processing from 'Excel' and 'SPSS' to R.
	"""
	
	homepage = "https://gdemin.github.io/expss/"
	cran = "expss" 

	version("0.11.6", md5="efc3b006f1438a52987897b5d125d5e1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-maditr@0.8.2:", type=("build", "run"))
	depends_on("r-data-table@1.12.6:", type=("build", "run"))
	depends_on("r-htmltable@1.11:", type=("build", "run"))
	depends_on("r-matrixstats@0.51:", type=("build", "run"))
