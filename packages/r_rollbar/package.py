# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRollbar(RPackage):
	"""Error Tracking and Logging

	Reports errors and messages to Rollbar, the error tracking platform <https://rollbar.com>.
	"""
	
	cran = "rollbar" 

	version("0.1.0", md5="ffca40695f9747dcbf9a3191fc4848ca")

	depends_on("r-httr", type=("build", "run"))
