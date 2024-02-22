# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinancialinstrument(RPackage):
	"""Financial Instrument Model Infrastructure and Meta-Data

	Infrastructure for defining meta-data and
    relationships for financial instruments.
	"""
	
	homepage = "https://github.com/braverock/FinancialInstrument"
	cran = "FinancialInstrument" 

	version("1.3.1", md5="af253e3ec6673802d759e78b44b926f9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-quantmod@0.4.3:", type=("build", "run"))
	depends_on("r-zoo@1.7.5:", type=("build", "run"))
	depends_on("r-xts@0.10.0:", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
