# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErpEasy(RPackage):
	"""Event-Related Potential (ERP) Data Exploration Made Easy

	A set of user-friendly functions to aid in organizing, plotting
    and analyzing event-related potential (ERP) data.  Provides an easy-to-learn
    method to explore ERP data. Should be useful to those without a background
    in computer programming, and to those who are new to ERPs (or new to the
    more advanced ERP software available). Emphasis has been placed on highly
    automated processes using functions with as few arguments as possible.
    Expects processed (cleaned) data.
	"""
	
	homepage = "https://github.com/mooretm/erp.easy"
	cran = "erp.easy" 

	version("1.1.0", md5="7420797048c544d17c1dcf034b42c4d3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-signal@0.7.6:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))
