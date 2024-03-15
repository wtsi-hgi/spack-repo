# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaskscheduler(RPackage):
	"""Schedule R Scripts and Processes with the Windows Task Scheduler

	Schedule R scripts/processes with the Windows task scheduler. This
    allows R users to automate R processes on specific time points from R itself.
	"""
	
	homepage = "https://github.com/bnosac/taskscheduleR"
	cran = "taskscheduleR" 

	version("1.8", md5="2e1a055a381e9665848895748de2c0a4")

	depends_on("r-data-table", type=("build", "run"))
