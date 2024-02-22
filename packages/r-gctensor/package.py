# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGctensor(RPackage):
	"""Generalized Coupled Tensor Factorization

	Multiple matrices/tensors can be specified and decomposed simultaneously by Probabilistic Latent Tensor Factorisation (PLTF). See the reference section of GitHub README.md <https://github.com/rikenbit/gcTensor>, for details of the method.
	"""
	
	homepage = "https://github.com/rikenbit/gcTensor"
	cran = "gcTensor" 

	version("1.0.0", md5="0bcb33093cefefffb1acf0a90ad1f7bf")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-einsum", type=("build", "run"))
