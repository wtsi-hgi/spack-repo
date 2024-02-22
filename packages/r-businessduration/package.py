# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBusinessduration(RPackage):
	"""Calculates Business Duration Between Two Dates

	Calculates business duration between two dates. This excluding weekends, public holidays and non-business hours.
	"""
	
	cran = "BusinessDuration" 

	version("0.2.0", md5="7abe66dcfc3f006ced6a4764958a5ff2")

	depends_on("r-chron", type=("build", "run"))
