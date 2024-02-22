# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoldfish(RPackage):
	"""Statistical Network Models for Dynamic Network Data

	Tools for fitting statistical network models to dynamic network data.
   Can be used for fitting both dynamic network actor models ('DyNAMs') and
   relational event models ('REMs').
   Stadtfeld, Hollway, and Block (2017a) <doi:10.1177/0081175017709295>,
   Stadtfeld, Hollway, and Block (2017b) <doi:10.1177/0081175017733457>,
   Stadtfeld and Block (2017) <doi:10.15195/v4.a14>,
   Hoffman et al. (2020) <doi:10.1017/nws.2020.3>.
	"""
	
	homepage = "https://snlab-ch.github.io/goldfish/"
	cran = "goldfish" 

	version("1.6.4", md5="664501daf051e2191c9e3585efd4c0e6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
