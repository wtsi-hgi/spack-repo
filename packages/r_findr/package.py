# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFindr(RPackage):
	"""Find Code Snippets, R Scripts, R Markdown, PDF and Text Files
with Pattern Matching

	Scans all directories and subdirectories of a path for code snippets, R scripts,
    R Markdown, PDF or text files containing a specific pattern.  Files found can be copied to a new folder.
	"""
	
	cran = "findR" 

	version("0.2.1", md5="4db624ae695bbfa0ddb3efd6577945eb")

	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
