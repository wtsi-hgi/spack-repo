# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmstat4(RPackage):
	"""Access to Teaching Materials from a ZIP File or GitHub

	Provides access to teaching materials for various statistics courses, including R programs, 
    Shiny apps, data, and PDF/HTML documents. These materials are stored on the Internet as a ZIP file 
    (e.g., in a GitHub repository) and can be downloaded and displayed or run locally. The content of the ZIP file 
    is temporarily or permanently stored. By default, the package uses the GitHub repository 
    'sigbertklinke/mmstat4.data.' Additionally, the package includes 'association_measures.R' 
    from the archived package 'ryouready' by Mark Heckman and some auxiliary functions.
	"""
	
	cran = "mmstat4" 

	version("0.1.6", md5="f36684dee0ba96ecc57dbb2ef1754b81", url="https://cran.r-project.org/src/contrib/mmstat4_0.1.6.tar.gz")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
