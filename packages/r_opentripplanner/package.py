# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpentripplanner(RPackage):
	"""Setup and connect to 'OpenTripPlanner'

	Setup and connect to 'OpenTripPlanner' (OTP) <http://www.opentripplanner.org/>.
    OTP is an open source platform for multi-modal and multi-agency
    journey planning written in 'Java'. The package allows you to manage a local version or 
    connect to remote OTP server to find walking, cycling, driving, or transit routes.
    This package has been peer-reviewed by rOpenSci (v. 0.2.0.0).
	"""
	
	homepage = "https://github.com/ropensci/opentripplanner"
	cran = "opentripplanner" 

	version("0.5.1", md5="f078c2a16663ada4db2c4f2297b5abca")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-googlepolylines", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rcppsimdjson@0.1.2:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-sf@0.9.3:", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
