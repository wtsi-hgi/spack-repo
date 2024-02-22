# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTablematrix(RPackage):
	"""Combines 'data.table' and 'matrix' Classes

	Provides two classes extending 'data.table' class. Simple
    'tableList' class wraps 'data.table' and any additional structures together.
    More complex 'tableMatrix' class combines 'data.table' and
    'matrix'. See <http://github.com/InferenceTechnologies/tableMatrix> for more
    information and examples.
	"""
	
	cran = "tableMatrix" 

	version("0.82.0", md5="ae365656f22757fd7a0246682ab95289")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
