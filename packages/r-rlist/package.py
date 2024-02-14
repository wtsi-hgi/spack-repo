# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlist(RPackage):
	"""A Toolbox for Non-Tabular Data Manipulation

	Provides a set of functions for data manipulation with
    list objects, including mapping, filtering, grouping, sorting,
    updating, searching, and other useful functions. Most functions
    are designed to be pipeline friendly so that data processing with
    lists can be chained.
	"""
	
	homepage = "https://renkun-ken.github.io/rlist/"
	cran = "rlist" 

	version("0.4.6.2", md5="c924e1fdb662d699803a67aa63cf3c94")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
