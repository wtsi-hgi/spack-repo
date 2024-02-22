# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakeit(RPackage):
	"""Run R Scripts if Needed

	Automation tool to run R scripts if needed, based on last modified
  time. Implemented in base R with no additional software requirements,
  organizational overhead, or structural requirements. In short: run an R script
  if underlying files have changed, otherwise do nothing.
	"""
	
	homepage = "https://github.com/arni-magnusson/makeit"
	cran = "makeit" 

	version("1.0.1", md5="6b0292de41ec1e319ff28db1e93f035c")

