# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsdam(RPackage):
	"""Forward Stepwise Deep Autoencoder-Based Monotone NLDR

	FS-DAM performs feature extraction through latent variables identification. Implementation is based on autoencoders with monotonicity and orthogonality constraints.
	"""
	
	cran = "FSDAM" 

	version("2024.1-30", md5="2139aa8ec5db7f390e5ec6ebb315721f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kyotil", type=("build", "run"))
	depends_on("r-reticulate@1.10:", type=("build", "run"))
