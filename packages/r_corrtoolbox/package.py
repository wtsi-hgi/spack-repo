# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrtoolbox(RPackage):
	"""Modeling Correlational Magnitude Transformations in
Discretization Contexts

	Modeling the correlation transitions under specified distributional assumptions within the realm of discretization in the context of the latency and threshold concepts. The details of the method are explained in Demirtas, H. and Vardar-Acar, C. (2017) <DOI:10.1007/978-981-10-3307-0_4>.
	"""
	
	cran = "CorrToolBox" 

	version("1.6.4", md5="be22e5b0c39bc54cc7fa2265990897db")

	depends_on("r-binnonnor", type=("build", "run"))
	depends_on("r-binordnonnor", type=("build", "run"))
	depends_on("r-genord", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
