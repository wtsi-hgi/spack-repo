# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTable1(RPackage):
	"""Tables of Descriptive Statistics in HTML

	Create HTML tables of descriptive statistics, as one would expect
    to see as the first table (i.e. "Table 1") in a medical/epidemiological journal
    article.
	"""
	
	homepage = "https://github.com/benjaminrich/table1"
	cran = "table1" 

	version("1.4.3", md5="68a0fb1d7b37fb8edd7e36360bdb0741", url="https://cran.r-project.org/src/contrib/table1_1.4.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
