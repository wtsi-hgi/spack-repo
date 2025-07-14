# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDelayedtensor(RPackage):
	"""R package for sparse and out-of-core arithmetic and decomposition of Tensor

	DelayedTensor operates Tensor arithmetic directly on DelayedArray object. DelayedTensor provides some generic function related to Tensor arithmetic/decompotision and dispatches it on the DelayedArray class. DelayedTensor also suppors Tensor contraction by einsum function, which is inspired by numpy einsum.
	"""
	
	bioc = "DelayedTensor"

	version("1.14.0", commit="85b592f821eb9632d37d06b6cb1999ba4ac1643e")
	version("1.8.0", commit="4663e70fbfca6f8d0dad8ec205b1993e23ed85ae")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-delayedrandomarray", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-einsum", type=("build", "run"))
