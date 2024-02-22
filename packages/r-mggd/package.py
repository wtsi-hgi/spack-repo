# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMggd(RPackage):
	"""Multivariate Generalised Gaussian Distribution; Kullback-Leibler
Divergence

	Distance between multivariate generalised Gaussian distributions, as presented by N. Bouhlel and A. Dziri (2019) <doi:10.1109/LSP.2019.2915000>. Manipulation of multivariate generalised Gaussian distributions (methods presented by Gomez, Gomez-Villegas and Marin (1998) <doi:10.1080/03610929808832115> and Pascal, Bombrun, Tourneret and Berthoumieu (2013) <doi:10.1109/TSP.2013.2282909>).
	"""
	
	homepage = "https://forgemia.inra.fr/imhorphen/mggd"
	cran = "mggd" 

	version("1.1.0", md5="d806950b05a94ddfe44743d467fa44bd")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
