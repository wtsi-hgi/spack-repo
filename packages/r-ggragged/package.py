# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgragged(RPackage):
	"""Ragged Grids for 'ggplot2'

	Extend 'ggplot2' facets to panel layouts arranged in a grid
    with ragged edges. facet_ragged_rows() groups panels in rows of
    (potentially) varying lengths, facet_ragged_cols() does the same for
    columns. These can be useful, for example, to represent nested or
    partially crossed relationships between faceting variables.
	"""
	
	homepage = "https://github.com/mikmart/ggragged"
	cran = "ggragged" 

	version("0.1.0", md5="a94ba166334389bb6186b190c6382bd6")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
