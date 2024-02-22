# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTstools(RPackage):
	"""A Time Series Toolbox for Official Statistics

	Plot official statistics' time series conveniently: automatic
    legends, highlight windows, stacked bar chars with positive and
    negative contributions, sum-as-line option, two y-axes with automatic
    horizontal grids that fit both axes and other popular chart types.
    'tstools' comes with a plethora of defaults to let you plot without
    setting an abundance of parameters first, but gives you the
    flexibility to tweak the defaults. In addition to charts, 'tstools'
    provides a super fast, 'data.table' backed time series I/O that allows
    the user to export / import long format, wide format and transposed
    wide format data to various file types.
	"""
	
	homepage = "https://github.com/KOF-ch/tstools"
	cran = "tstools" 

	version("0.4.3", md5="5db49519452e5e39fd8d2755367bccca")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-zoo@1.7.12:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
