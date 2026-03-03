# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccumulate(RPackage):
	"""Split-Apply-Combine with Dynamic Groups

	Estimate group aggregates, where one can set user-defined conditions
   that each group of records must satisfy to be suitable for aggregation. If
   a group of records is not suitable, it is expanded using a collapsing scheme
   defined by the user. 
	"""
	
	homepage = "https://github.com/markvanderloo/accumulate"
	cran = "accumulate" 

	version("0.9.3", md5="4e731b84527f3701b17786d835d93774")

	depends_on("r@3.5:", type=("build", "run"))
