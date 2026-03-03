# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcesscheckr(RPackage):
	"""Rule-Based Conformance Checking of Business Process Event Data

	Check compliance of event-data from (business) processes with respect to specified rules. Rules supported are of three types: frequency (activities that should (not) happen x number of times), order (succession between activities) and exclusiveness (and and exclusive choice between activities).
	"""
	
	homepage = "https://bupar.net/"
	cran = "processcheckR" 

	version("0.1.4", md5="5a7bfc8f5118dfecab893f939342621c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-bupar@0.5.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-edear@0.9:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
