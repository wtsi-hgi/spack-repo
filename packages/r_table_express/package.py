# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTableExpress(RPackage):
	"""Build 'data.table' Expressions with Data Manipulation Verbs

	A specialization of 'dplyr' data manipulation verbs that parse and build expressions
    which are ultimately evaluated by 'data.table', letting it handle all optimizations. A set of
    additional verbs is also provided to facilitate some common operations on a subset of the data.
	"""
	
	homepage = "https://asardaes.github.io/table.express/"
	cran = "table.express" 

	version("0.4.2", md5="6f1f04e0192011031e9b5fcd1cdac24b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
