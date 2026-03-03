# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrdna(RPackage):
	"""Finding Associations in Position-Wise Aligned DNA Sequence
Dataset

	Can be useful for finding associations among different positions in a position-wise aligned sequence dataset. The approach adopted for finding associations among positions is based on the latent multivariate normal distribution.
	"""
	
	cran = "corrDNA" 

	version("1.0.1", md5="386104d5cab16d1623658b145c950e36")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
