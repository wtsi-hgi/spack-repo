# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWktmo(RPackage):
	"""Converting Weekly Data to Monthly Data

	Converts weekly data to monthly data.
     Users can use three types of week formats: ISO week, epidemiology week (epi week) and calendar date. 
	"""
	
	cran = "wktmo" 

	version("1.0.5", md5="86d1e870fb4122e6c0283735ed3ac980")

	depends_on("r@3.4:", type=("build", "run"))
