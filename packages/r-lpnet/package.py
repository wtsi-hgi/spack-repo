# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpnet(RPackage):
	"""Linear Programming Model for Network Inference

	lpNet aims at infering biological networks, in particular signaling and gene networks. For that it takes perturbation data, either steady-state or time-series, as input and generates an LP model which allows the inference of signaling networks. For parameter identification either leave-one-out cross-validation or stratified n-fold cross-validation can be used.
	"""
	
	bioc = "lpNet" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/lpNet_2.34.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/lpNet/lpNet_2.34.2.tar.gz"]

	version("2.34.2", md5="98de40db5eda03f2ae3b35cf04c6882c")

	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
