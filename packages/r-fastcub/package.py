# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastcub(RPackage):
	"""Fast Estimation of CUB Models via Louis' Identity

	For ordinal rating data, consider the accelerated EM algorithm to estimate and test models within the family of
    CUB models (where CUB stands for Combination of a 
	discrete Uniform and a shifted Binomial distributions). The procedure is built upon Louis' identity for the observed information matrix. Best-subset variable selection is then implemented since it becomes more feasible from the computational point of view.
	"""
	
	cran = "FastCUB" 

	version("0.0.3", md5="7646bfec4b4dae546045c877f166f98b")
	version("0.0.2", md5="481c248e1f6882af1e478abd928ca59a")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-cub", type=("build", "run"))
