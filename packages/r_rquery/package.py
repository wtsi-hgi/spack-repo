# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRquery(RPackage):
	"""Relational Query Generator for Data Manipulation at Scale

	A piped query generator based on Edgar F. Codd's relational
    algebra, and on production experience using 'SQL' and 'dplyr' at big data
    scale.  The design represents an attempt to make 'SQL' more teachable by
    denoting composition by a sequential pipeline notation instead of nested
    queries or functions.   The implementation delivers reliable high 
    performance data processing on large data systems such as 'Spark',
    databases, and 'data.table'. Package features include: data processing trees
    or pipelines as observable objects (able to report both columns
    produced and columns used), optimized 'SQL' generation as an explicit
    user visible table modeling step, plus explicit query reasoning and checking.
	"""
	
	homepage = "https://github.com/WinVector/rquery/"
	cran = "rquery" 

	version("1.4.99", md5="933b8a7eb8906c5d85cc428ee1c53e48")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-wrapr@2.0.9:", type=("build", "run"))
