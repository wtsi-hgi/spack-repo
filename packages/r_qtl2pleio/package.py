# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtl2pleio(RPackage):
	"""Testing Pleiotropy in Multiparental Populations

	We implement an
    adaptation of Jiang & Zeng's (1995) <https://www.genetics.org/content/140/3/1111> likelihood ratio test for testing
    the null hypothesis of pleiotropy against the alternative hypothesis,
    two separate quantitative trait loci. The test differs from that in Jiang & Zeng (1995) <https://www.genetics.org/content/140/3/1111> 
    and that in Tian et al. (2016) <doi:10.1534/genetics.115.183624> in
    that our test accommodates multiparental populations.
	"""
	
	homepage = "https://github.com/fboehm/qtl2pleio"
	cran = "qtl2pleio" 

	version("1.4.3", md5="dea0f0e4003fd9915ddda48c302c286d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gemma2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
