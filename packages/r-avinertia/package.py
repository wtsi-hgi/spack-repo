# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAvinertia(RPackage):
	"""Calculate the Inertial Properties of a Flying Bird

	
    Tools to compute the center of gravity and moment of inertia tensor of any 
    flying bird. The tools function by modeling a bird as a composite structure 
    of simple geometric objects. This requires detailed morphological 
    measurements of bird specimens although those obtained for the associated 
    paper have been included in the package for use. Refer to the vignettes and 
    supplementary material for detailed information on the package function.
	"""
	
	homepage = "https://github.com/charvey23/AvInertia"
	cran = "AvInertia" 

	version("0.0.2", md5="0380aa25f3d4087864ecc70a95239dcc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
