# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTableGlue(RPackage):
	"""Make and Apply Customized Rounding Specifications for Tables

	Translate double and integer valued data into
    character values formatted for tabulation in manuscripts
    or other types of academic reports. 
	"""
	
	homepage = "https://github.com/bcjaeger/table.glue"
	cran = "table.glue" 

	version("0.0.3", md5="dfbe9d109a2335d7dfb771a902b35cf6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
