# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeform(RPackage):
	"""Spatial Deformation and Dimension Expansion Gaussian Processes

	Methods for fitting nonstationary Gaussian process models by spatial deformation, as introduced by Sampson and Guttorp (1992) <doi:10.1080/01621459.1992.10475181>, and by dimension expansion, as introduced by Bornn et al. (2012) <doi:10.1080/01621459.2011.646919>. Low-rank thin-plate regression splines, as developed in Wood, S.N. (2003) <doi:10.1111/1467-9868.00374>, are used to either transform co-ordinates or create new latent dimensions.
	"""
	
	cran = "deform" 

	version("1.0.0", md5="33904d79855a4751c5bdcb5519443b2d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
