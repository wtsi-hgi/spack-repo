# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrycatchlog(RPackage):
	"""Advanced 'tryCatch()' and 'try()' Functions

	Advanced tryCatch() and try() functions for better error handling
             (logging, stack trace with source code references and support for post-mortem analysis via dump files).
	"""
	
	homepage = "https://github.com/aryoda/tryCatchLog"
	cran = "tryCatchLog" 

	version("1.3.1", md5="8af32996a44c67f3989ecfb37903e8c4")

	depends_on("r@3.1:", type=("build", "run"))
