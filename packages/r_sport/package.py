# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSport(RPackage):
	"""Sequential Pairwise Online Rating Techniques

	Calculates ratings for two-player or 
  multi-player challenges. Methods included in package such as are able to 
  estimate ratings (players strengths) and their evolution in time, also able to 
  predict output of challenge. Algorithms are based on Bayesian Approximation 
  Method, and they don't involve any matrix inversions nor likelihood estimation. 
  Parameters are updated sequentially, and computation doesn't require any 
  additional RAM to make estimation feasible. Additionally, base of the package 
  is written in C++ what makes sport computation even faster. Methods used in the 
  package refer to Mark E. Glickman (1999) 
  <http://www.glicko.net/research/glicko.pdf>; 
  Mark E. Glickman (2001) <doi:10.1080/02664760120059219>; 
  Ruby C. Weng, Chih-Jen Lin (2011) <https://www.jmlr.org/papers/volume12/weng11a/weng11a.pdf>; 
  W. Penny, Stephen J. Roberts (1999) <doi:10.1109/IJCNN.1999.832603>.
	"""
	
	homepage = "https://github.com/gogonzo/sport"
	cran = "sport" 

	version("0.2.1", md5="c0bb98cea170052ef73e3552e5fb8222")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
