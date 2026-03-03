# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqn(RPackage):
	"""Subset Quantile Normalization

	Normalization based a subset of negative control probes as
        described in 'Subset quantile normalization using negative
        control features'. Wu Z, Aryee MJ, J Comput Biol. 2010
        Oct;17(10):1385-95 [PMID 20976876].
	"""
	
	cran = "SQN" 

	version("1.0.6", md5="4f525c5cc5d254b03c180fbc4136061e")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-mclust@3.2:", type=("build", "run"))
	depends_on("r-nor1mix@1.0.7:", type=("build", "run"))
