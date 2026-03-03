# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElorating(RPackage):
	"""Animal Dominance Hierarchies by Elo Rating

	Provides functions to quantify animal dominance hierarchies. The major focus is on Elo rating and its ability to deal with temporal dynamics in dominance interaction sequences. For static data, David's score and de Vries' I&SI are also implemented. In addition, the package provides functions to assess transitivity, linearity and stability of dominance networks. See Neumann et al (2011) <doi:10.1016/j.anbehav.2011.07.016> for an introduction.
	"""
	
	homepage = "https://github.com/gobbios/EloRating"
	cran = "EloRating" 

	version("0.46.11", md5="58b0bfd2bf57cd1946e71c9f1faa31c1")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
