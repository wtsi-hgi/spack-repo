# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPde(RPackage):
	"""Extract Tables and Sentences from PDFs with User Interface

	The PDE (Pdf Data Extractor) allows the extraction of 
    information and tables optionally based on search words from 
    PDF (Portable Document Format) files and enables the visualization 
    of the results, both by providing a convenient user-interface. 
	"""
	
	cran = "PDE" 

	version("1.4.8", md5="d908dd09eab2f6fc008d9623edb4ce36")

	depends_on("r-tcltk2@1.2.11:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
