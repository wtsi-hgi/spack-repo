# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUptimerobot(RPackage):
	"""Access the UptimeRobot Ping API

	Provide a set of wrappers to call all the endpoints of UptimeRobot API
  which includes various kind of ping, keep-alive and speed tests.
  See <https://uptimerobot.com/> for more information.
	"""
	
	homepage = "https://gabrielebaldassarre.com/r/uptimerobot"
	cran = "uptimeRobot" 

	version("1.0.0", md5="dea42eabeba4c0e72267cf9373227edb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
