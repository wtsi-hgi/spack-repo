# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcfun(RPackage):
	"""Functions for 'Ecdat'

	Functions and vignettes to update 
    data sets in 'Ecdat' and to create, manipulate, 
    plot, and analyze those and similar data sets.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "Ecfun" 

	version("0.3-2", md5="8ab9376580e21f37664b5675497e33af")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-tis", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-bma", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
