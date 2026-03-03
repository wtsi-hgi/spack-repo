# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdfminer(RPackage):
	"""Read Portable Document Format (PDF) Files

	Provides an interface to 'PDFMiner' <https://github.com/pdfminer/pdfminer.six> 
    a 'Python' package for extracting information from 'PDF'-files. 
    'PDFMiner' has the goal to get all information available in a 'PDF'-file, 
    position of the characters, font type, font size and informations about lines. 
    Which makes it the perfect starting point for extracting tables from 'PDF'-files.
    More information can be found in the package 'README'-file.
	"""
	
	cran = "pdfminer" 

	version("1.0", md5="6d2e2e7fb95567b1f980a12af3c810cd")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("python@3.6:", type=("build", "link", "run"))
	depends_on("py-pandas", type=("build", "link", "run"))
