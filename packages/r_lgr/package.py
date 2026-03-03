# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLgr(RPackage):
	"""A Fully Featured Logging Framework

	A flexible, feature-rich yet light-weight logging
    framework based on 'R6' classes. It supports hierarchical loggers,
    custom log levels, arbitrary data fields in log events, logging to
    plaintext, 'JSON', (rotating) files, memory buffers. For extra
    appenders that support logging to databases, email and push
    notifications see the the package lgr.app.
	"""
	
	homepage = "https://s-fleck.github.io/lgr/"
	cran = "lgr" 

	version("0.4.4", md5="0804a98afca9506aab1ea2cde5db7c8a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
