# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdLog(RPackage):
	"""Produces Markdown Log File with a Built-in Function Call

	Produces clean and neat Markdown log file
    and also provide an argument to include the function call inside the Markdown log.
	"""
	
	homepage = "https://github.com/haghish/md.log"
	cran = "md.log" 

	version("0.2.0", md5="9fb798d4633619fd91bc8c039dc9af50")

	depends_on("r-futile-logger", type=("build", "run"))
