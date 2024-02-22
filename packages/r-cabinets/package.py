# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCabinets(RPackage):
	"""Project Specific Workspace Organization Templates

	Creates project specific directory and file templates that are 
 written to a .Rprofile file. Upon starting a new R session, these templates 
 can be used to streamline the creation of new directories that are 
 standardized to the user's preferences and can include the initiation of a 
 git repository, an RStudio R project, and project-local dependency management 
 with the 'renv' package.  
	"""
	
	homepage = "https://github.com/nt-williams/cabinets"
	cran = "cabinets" 

	version("0.6.0", md5="54387a500c204c3860d2d55657c642a1")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
