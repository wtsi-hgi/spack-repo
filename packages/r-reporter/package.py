# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReporter(RPackage):
	"""Creates Statistical Reports

	Contains functions to create regulatory-style statistical reports.
    Originally designed to create tables, listings, and figures for the 
    pharmaceutical, biotechnology, and medical device industries, these
    reports are generalized enough that they could be used in any industry.
    Generates text, rich-text, PDF, HTML, and Microsoft Word file formats.  
    The package specializes 
    in printing wide and long tables with automatic page wrapping and splitting.  
    Reports can be produced with a minimum of function calls, and without 
    relying on other table packages.  The package supports titles, footnotes, 
    page header, page footers, spanning headers, page by variables, 
    and automatic page numbering.
	"""
	
	homepage = "https://reporter.r-sassy.org"
	cran = "reporter" 

	version("1.4.4", md5="abc6f9625c48459084140a0da1c333e7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-common@1.1:", type=("build", "run"))
	depends_on("r-fmtr@1.5.8:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
