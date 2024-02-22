# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRllama(RPackage):
	"""Access and Analyze Data from 'DeFiLlama'

	Provides an interface to access and analyze data from
    'DeFiLlama'<https://defillama.com>. This package simplifies the
    process of fetching and manipulating 'DeFiLlama' data for further
    analysis and visualization.
	"""
	
	homepage = "https://github.com/AlexTwoR/rllama"
	cran = "rllama" 

	version("0.4.4", md5="e8483533997492a6d4d7cc7b8b08f2ff")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
