# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDedupewider(RPackage):
	"""Deduplication Across Multiple Columns

	Duplicated data can exist in different rows and columns and user may need to
    treat observations (rows) connected by duplicated data as one observation,
    e.g. companies can belong to one family (and thus: be one company) by sharing
    some telephone numbers. This package allows to find connected rows
    based on data on chosen columns and collapse it into one row.
	"""
	
	homepage = "https://github.com/gsmolinski/dedupewider"
	cran = "dedupewider" 

	version("0.1.0", md5="751c325bbb7389ac15f451f5302cf466")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
