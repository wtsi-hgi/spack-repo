# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosinor2(RPackage):
	"""Extended Tools for Cosinor Analysis of Rhythms

	Statistical procedures for calculating population–mean cosinor, non–stationary cosinor, estimation of best–fitting period, tests of population rhythm differences and more. See Cornélissen, G. (2014). <doi:10.1186/1742-4682-11-16>.
	"""
	
	homepage = "https://github.com/amutak/cosinor2"
	cran = "cosinor2" 

	version("0.2.1", md5="fcd1ade9512bce02d16e7101344eec15", url="https://cran.r-project.org/src/contrib/cosinor2_0.2.1.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cosinor@1.1:", type=("build", "run"))
	depends_on("r-cowplot@0.9.3:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-matrixstats@0.52.2:", type=("build", "run"))
	depends_on("r-hmisc@4.0.3:", type=("build", "run"))
