# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcccd(RPackage):
	"""Class Cover Catch Digraph Classification

	Fit Class Cover Catch Digraph Classification models that can be 
    used in machine learning. Pure and proper and random walk approaches are 
    available. Methods are explained in Priebe et al. (2001) 
    <doi:10.1016/S0167-7152(01)00129-8>, Priebe et al. (2003) 
    <doi:10.1007/s00357-003-0003-7>, and Manukyan and Ceyhan (2016) 
    <doi:10.48550/arXiv.1904.04564>.
	"""
	
	cran = "rcccd" 

	version("0.3.2", md5="1d10e292a9c76245bf23bbf768d93da5")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
