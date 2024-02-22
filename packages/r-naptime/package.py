# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaptime(RPackage):
	"""A Flexible and Robust Sys.sleep() Replacement

	Provides a near drop-in replacement for base::Sys.sleep() that allows more types of input
    to produce delays in the execution of code and can silence/prevent typical sources of error.
	"""
	
	homepage = "URL:"
	cran = "naptime" 

	version("1.3.0", md5="adca61d59dda0c8559d1f6af0229e6f5")

	depends_on("r-lubridate", type=("build", "run"))
