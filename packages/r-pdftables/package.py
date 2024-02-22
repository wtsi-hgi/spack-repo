# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdftables(RPackage):
	"""Programmatic Conversion of PDF Tables

	Allows the user to convert PDF tables to formats more amenable to
  analysis ('.csv', '.xml', or '.xlsx') by wrapping the PDFTables API.
  In order to use the package, the user needs to sign up for an API account
  on the PDFTables website (<https://pdftables.com/pdf-to-excel-api>).
  The package works by taking a PDF file as input, uploading it to PDFTables,
  and returning a file with the extracted data.
	"""
	
	homepage = "https://www.github.com/expersso/pdftables"
	cran = "pdftables" 

	version("0.1", md5="aee4a0ae3d840cdde0322c861f984b7d")

	depends_on("r-httr", type=("build", "run"))
