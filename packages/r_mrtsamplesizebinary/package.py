# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrtsamplesizebinary(RPackage):
	"""Sample Size Calculator for MRT with Binary Outcomes

	Provides a sample size calculator for micro-randomized trials (MRTs) with binary outcomes based on Cohn et al. (2023) <doi:10.1002/sim.9748>. Also provides a power calculator when the sample size is input by the user.
	"""
	
	cran = "MRTSampleSizeBinary" 

	version("0.1.2", md5="0e9cd125113e347d70ea8d2756739d0d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
