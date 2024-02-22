# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBicausality(RPackage):
	"""Binary Causality Inference Framework

	A framework to infer causality on binary data using techniques in frequent pattern mining and estimation statistics. Given a set of individual vectors S={x} where x(i) is a realization value of binary variable i, the framework infers empirical causal relations of binary variables i,j from S in a form of causal graph G=(V,E) where V is a set of nodes representing binary variables and there is an edge from i to j in E if the variable i causes j. The framework determines dependency among variables as well as analyzing confounding factors before deciding whether i causes j.  The publication of this package is at Chainarong Amornbunchornvej, Navaporn Surasvadi, Anon Plangprasopchok, and Suttipong Thajchayapong (2023) <doi:10.1016/j.heliyon.2023.e15947>.
	"""
	
	homepage = "https://github.com/DarkEyes/BiCausality"
	cran = "BiCausality" 

	version("0.1.4", md5="b2f87f3c84bd1e5e6754bc265b672af0")

	depends_on("r@3.5:", type=("build", "run"))
