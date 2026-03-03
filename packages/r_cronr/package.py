# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCronr(RPackage):
	"""Schedule R Scripts and Processes with the 'cron' Job Scheduler

	Create, edit, and remove 'cron' jobs on your unix-alike system. The package provides a set of easy-to-use wrappers
    to 'crontab'. It also provides an RStudio add-in to easily launch and schedule your scripts.
	"""
	
	homepage = "https://github.com/bnosac/cronR"
	cran = "cronR" 

	version("0.6.5", md5="ca53068888a71b715a0d5d46d3bd0d58")

	depends_on("r-digest", type=("build", "run"))
	depends_on("cronie", type=("build", "link", "run"))
