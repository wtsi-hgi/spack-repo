# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIxpopdymod(RPackage):
	"""Framework for Tick Population and Infection Modeling

	Code to specify, run, and then visualize and analyze the results of 
    Ixodidae (hard-bodied ticks) population and infection dynamics models. Such 
    models exist in the literature, but the source code to run them is not 
    always available. 'IxPopDyMod' provides an easy way for these models to be 
    written and shared.
	"""
	
	homepage = "https://github.com/dallenmidd/IxPopDyMod"
	cran = "IxPopDyMod" 

	version("0.3.0", md5="014bd07862108198bf66c4bf0ea17b7f")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
