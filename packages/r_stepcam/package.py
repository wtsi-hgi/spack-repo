# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepcam(RPackage):
	"""ABC-SMC Inference of STEPCAM

	Collection of model estimation, and model plotting functions 
             related to the STEPCAM family of community assembly models. 
             STEPCAM is a STEPwise Community Assembly Model that infers 
             the relative contribution of Dispersal Assembly, Habitat Filtering 
             and Limiting Similarity from a dataset consisting of the 
             combination of trait and abundance data. See also <http://onlinelibrary.wiley.com/wol1/doi/10.1890/14-0454.1/abstract> for more information.
	"""
	
	homepage = "https://github.com/thijsjanzen/STEPCAM"
	cran = "STEPCAM" 

	version("1.2", md5="2b27d545c27434def26d04c447108f4e")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-fd", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
