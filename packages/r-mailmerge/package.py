# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMailmerge(RPackage):
	"""Mail Merge Using R Markdown Documents and 'gmailr'

	Perform a mail merge (mass email) using the message defined in 
    markdown, the recipients in a 'csv' file, and gmail as the mailing engine. 
    With this package you can parse markdown documents as the body of email, and 
    the 'yaml' header to specify the subject line of the email.  Any '{}' braces 
    in the email will be encoded with 'glue::glue()'. You can preview the email 
    in the RStudio viewer pane, and send (draft) email using 'gmailr'.
	"""
	
	homepage = "https://andrie.github.io/mailmerge/"
	cran = "mailmerge" 

	version("0.2.5", md5="55ca57d2242b7b913e35647a03feea8e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-commonmark", type=("build", "run"))
	depends_on("r-gmailr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-googledrive", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
