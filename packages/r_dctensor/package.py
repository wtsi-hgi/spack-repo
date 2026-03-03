# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDctensor(RPackage):
	"""Discrete Matrix/Tensor Decomposition

	Semi-Binary and Semi-Ternary Matrix Decomposition are performed based on Non-negative Matrix Factorization (NMF) and Singular Value Decomposition (SVD). For the details of the methods, see the reference section of GitHub README.md <https://github.com/rikenbit/dcTensor>.
	"""
	
	homepage = "https://github.com/rikenbit/dcTensor"
	cran = "dcTensor" 

	version("1.2.0", md5="7b88ca844910709a1f58ceae5075866f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-nntensor", type=("build", "run"))
