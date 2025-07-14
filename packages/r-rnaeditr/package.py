# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaeditr(RPackage):
	"""Statistical analysis of RNA editing sites and hyper-editing regions

	RNAeditr analyzes site-specific RNA editing events, as well as hyper-editing regions. The editing frequencies can be tested against binary, continuous or survival outcomes. Multiple covariate variables as well as interaction effects can also be incorporated in the statistical models.
	"""
	
	homepage = "https://github.com/TransBioInfoLab/rnaEditr"
	bioc = "rnaEditr"

	version("1.18.0", commit="6ce3b4d0ee53a8d5b2b8e7995565943b7ffd080e")
	version("1.12.0", commit="50458843ea45f405133a97755f666a3a0df22ea6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-bumphunter", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-logistf", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
