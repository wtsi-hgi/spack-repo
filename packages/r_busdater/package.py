# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBusdater(RPackage):
	"""Standard Date Calculations for Business

	Get a current financial year, start of current
    month, End of current month, start of financial year and end of it.
    Allow for offset from the date.
	"""
	
	homepage = "https://mickmioduszewski.github.io/busdater/"
	cran = "busdater" 

	version("0.2.0", md5="c2aac8922109143512df16f2443dd5f6")

	depends_on("r-lubridate", type=("build", "run"))
