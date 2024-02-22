# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestimizeapi(RPackage):
	"""Functions for Working with the 'www.estimize.com' Web Services

	Provides the user with functions to develop their trading strategy,
    uncover actionable trading ideas, and monitor consensus shifts with
    crowdsourced earnings and economic estimate data directly from
    <www.estimize.com>. Further information regarding the web services this
    package invokes can be found at <www.estimize.com/api>.
	"""
	
	homepage = "http://www.r-project.org"
	cran = "restimizeapi" 

	version("1.0.0", md5="e67ad20fc41a1ddc95f43448d7f31d94")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
