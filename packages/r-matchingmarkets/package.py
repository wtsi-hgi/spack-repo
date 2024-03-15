# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatchingmarkets(RPackage):
	"""Analysis of Stable Matchings

	Implements structural estimators to correct for
    the sample selection bias from observed outcomes in matching
    markets. This includes one-sided matching of agents into groups 
    (Klein, 2015) <https://www.econ.cam.ac.uk/research-files/repec/cam/pdf/cwpe1521.pdf> 
    as well as two-sided matching of students to schools 
    (Aue et al., 2020) <https://ftp.zew.de/pub/zew-docs/dp/dp20032.pdf>.
    The package also contains algorithms to find stable matchings
    in the three most common matching problems: the stable roommates
    problem (Irving, 1985) <doi:10.1016/0196-6774(85)90033-1>, 
    the college admissions problem (Gale and Shapley, 1962) <doi:10.2307/2312726>, 
    and the house allocation problem (Shapley and Scarf, 1974) <doi:10.1016/0304-4068(74)90033-0>.
	"""
	
	homepage = "https://matchingMarkets.org"
	cran = "matchingMarkets" 

	version("1.0-4", md5="290d5f3bda18232d0ee3aa60d2e87b80")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("openjdk", type=("build", "link", "run"))
