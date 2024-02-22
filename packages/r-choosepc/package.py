# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChoosepc(RPackage):
	"""Choose the Number of Principal Components via Recistruction
Error

	One way to choose the number of principal components is via the reconstruction error. This package is designed mainly for this purpose. Graphical representation is also supported, plus some other principal component analysis related functions. References include: Jolliffe I.T. (2002). Principal Component Analysis. <doi:10.1007/b98835> and Mardia K.V., Kent J.T. and Bibby J.M. (1979). Multivariate Analysis. ISBN: 978-0124712522. London: Academic Press.
	"""
	
	cran = "choosepc" 

	version("1.0", md5="9db27ae57ce5bbb8b8b8840ab5cb7487")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
