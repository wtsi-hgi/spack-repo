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

	version("1.2.3", md5="c8f8d03b5a39d27b472962e4fa6b5a5c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
