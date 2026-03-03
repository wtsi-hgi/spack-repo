# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlan(RPackage):
	"""Tools for Project Planning

	Supports the creation of 'burndown' charts and 'gantt' diagrams.
	"""
	
	homepage = "https://github.com/dankelley/plan"
	cran = "plan" 

	version("0.4-5", md5="9f424a0a6cfbe41226ca918116976d70")

	depends_on("r@2.15:", type=("build", "run"))
