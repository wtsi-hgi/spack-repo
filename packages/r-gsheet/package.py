# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsheet(RPackage):
	"""Download Google Sheets Using Just the URL

	Simple package to download Google Sheets using just the sharing
    link. Spreadsheets can be downloaded as a data frame, or as plain text to parse
    manually. Google Sheets is the new name for Google Docs Spreadsheets <https://www.google.com/sheets/about>.
	"""
	
	homepage = "https://github.com/maxconway/gsheet"
	cran = "gsheet" 

	version("0.4.5", md5="b6f07be4c3c8c74ec2195c311165c0f5")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
