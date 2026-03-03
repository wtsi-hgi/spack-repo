# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdaptools(RPackage):
	"""Tools for the 'qdap' Package

	A collection of tools associated with the 'qdap' package that may be useful outside of the
            context of text analysis.
	"""
	
	homepage = "https://github.com/trinker/qdapTools"
	cran = "qdapTools" 

	version("1.3.7", md5="b62aded06a3f85072a48e421c7f5dff6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
