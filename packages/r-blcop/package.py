# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlcop(RPackage):
	"""Black-Litterman and Copula Opinion Pooling Frameworks

	An implementation of the Black-Litterman Model and Attilio
    Meucci's copula opinion pooling framework as described in
    Meucci, Attilio (2005) <doi:10.2139/ssrn.848407>,
    Meucci, Attilio (2006) <doi:10.2139/ssrn.872577> and
    Meucci, Attilio (2008) <doi:10.2139/ssrn.1117574>.
	"""
	
	homepage = "https://github.com/mangothecat/BLCOP"
	cran = "BLCOP" 

	version("0.3.3", md5="db7df893026c087a758e3b5ef7e16226")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-runit@0.4.22:", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-fmultivar", type=("build", "run"))
	depends_on("r-fportfolio@3011.81:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
