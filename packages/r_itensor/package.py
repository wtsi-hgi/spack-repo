# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItensor(RPackage):
	"""ICA-Based Matrix/Tensor Decomposition

	Some functions for performing ICA, MICA, Group ICA, and Multilinear ICA are implemented.
    ICA, MICA/Group ICA, and Multilinear ICA extract statistically independent components from single matrix, multiple matrices, and single tensor, respectively.
    For the details of these methods, see the reference section of GitHub README.md <https://github.com/rikenbit/iTensor>.
	"""
	
	homepage = "https://github.com/rikenbit/iTensor"
	cran = "iTensor" 

	version("1.0.2", md5="7eb89ec14937ed6bb08ac8315e219d22")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-jointdiag", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-einsum", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-groupica", type=("build", "run"))
