# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndexconstruction(RPackage):
	"""Index Construction for Time Series Data

	Derivation of indexes for benchmarking purposes. A methodology with flexible number of constituents is implemented. Also functions for market capitalization and volume weighted indexes with fixed number of constituents are available. The main function of the package, indexComp(), provides the derived index, suitable for analysis purposes. The functions indexUpdate(), indexMemberSelection() and indexMembersUpdate() are components of indexComp() and enable one to construct and continuously update an index, e.g. for display on a website. The methodology behind the functions provided gets introduced in Trimborn and Haerdle (2018) <doi:10.1016/j.jempfin.2018.08.004>.
	"""
	
	cran = "IndexConstruction" 

	version("0.1-3", md5="5de834c4ed9c2b427a89c37f927dccbd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-rcppbdt", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
