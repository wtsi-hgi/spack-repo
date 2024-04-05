# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadtext(RPackage):
	"""Import and Handling for Plain and Formatted Text Files

	Functions for importing and handling text files and formatted text
    files with additional meta-data, such including '.csv', '.tab', '.json', '.xml',
    '.html', '.pdf', '.doc', '.docx', '.rtf', '.xls', '.xlsx', and others.
	"""
	
	homepage = "https://github.com/quanteda/readtext"
	cran = "readtext" 

	version("0.91", md5="4bc20ead09054bfaacc09acf9a3022ec")
	version("0.90", md5="7106035be06c804ec975e76bb2b6725c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-antiword", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite@0.9.10:", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-readods@1.7:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-streamr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-striprtf", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
