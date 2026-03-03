# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeededlda(RPackage):
	"""Seeded Sequential LDA for Topic Modeling

	Seeded Sequential LDA can classify sentences of texts into pre-define topics with a small number of seed words (Watanabe & Baturo, 2023) <doi:10.1177/08944393231178605>.
    Implements Seeded LDA (Lu et al., 2010) <doi:10.1109/ICDMW.2011.125> and Sequential LDA (Du et al., 2012) <doi:10.1007/s10115-011-0425-1> with the distributed LDA algorithm (Newman, et al., 2009) for parallel computing.
	"""
	
	homepage = "https://github.com/koheiw/seededlda"
	cran = "seededlda" 

	version("1.1.0", md5="d421963b70d74ec636d294210a3d17d5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-proxyc@0.3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
