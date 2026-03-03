# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogging(RPackage):
	"""R Logging Package

	Pure R implementation of the ubiquitous log4j package. It offers hierarchic 
  loggers, multiple handlers per logger, level based filtering, space handling in messages 
  and custom formatting.
	"""
	
	homepage = "https://github.com/WLOGSolutions/r-logging"
	cran = "logging" 

	version("0.10-108", md5="b72368fc427dc461d30ad6b8b4ba9482")

	depends_on("r@3.2:", type=("build", "run"))
