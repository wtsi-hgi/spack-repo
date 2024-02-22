# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbrokers(RPackage):
	"""R API to Interactive Brokers Trader Workstation

	Provides native R access to Interactive Brokers Trader Workstation API.
	"""
	
	cran = "IBrokers" 

	version("0.10-2", md5="f6573eb494ce8ba501fe254a0b63eb16")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
