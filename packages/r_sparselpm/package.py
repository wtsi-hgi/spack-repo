# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparselpm(RPackage):
	"""The Sparse Latent Position Model for Nonnegative Interaction
Data

	Models the nonnegative entries of a rectangular adjacency matrix using a sparse latent position model, as illustrated in Rastelli, R. (2018) "The Sparse Latent Position Model for nonnegative weighted networks" <arXiv:1808.09262>.
	"""
	
	cran = "SparseLPM" 

	version("1.0", md5="b64ad7bf0ae561379b14f81a33228e79")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
