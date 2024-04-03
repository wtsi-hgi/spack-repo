# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyinvoice(RPackage):
	"""Shiny App - Generate a Pdf Invoice with 'Rmarkdown'

	Generate an invoice containing a header with invoice number and businesses details. The invoice table contains
  any of: salary, one-liner costs, grouped costs. Under the table signature and bank account details appear. 
  Pages are numbered when more than one. Source .json and .Rmd files are editable in the app. A .csv file with raw data can be downloaded.
  This package includes functions for getting exchange rates between currencies based on 
  'quantmod' (Ryan and Ulrich, 2023 <https://CRAN.R-project.org/package=quantmod>).
	"""
	
	homepage = "https://github.com/fernandoroa/invoice-public"
	cran = "shinyInvoice" 

	version("0.0.5", md5="baa8216c3fb40ab525bb56179a014c27")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("pandoc@2.0:", type=("build", "link", "run"))
