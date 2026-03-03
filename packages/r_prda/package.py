# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrda(RPackage):
	"""Conduct a Prospective or Retrospective Design Analysis

	An implementation of the "Design Analysis" proposed by 
    Gelman and Carlin (2014) <doi:10.1177/1745691614551642>. It combines 
    the evaluation of Power-Analysis with other inferential-risks as 
    Type-M error (i.e. Magnitude) and Type-S error (i.e. Sign). See also
    Altoè et al. (2020) <doi:10.3389/fpsyg.2019.02893> and 
    Bertoldo et al. (2020) <doi:10.31234/osf.io/q9f86>.
	"""
	
	homepage = "https://claudiozandonella.github.io/PRDA/"
	cran = "PRDA" 

	version("1.0.0", md5="9a437d130094d83a60d7f18800b8288d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
