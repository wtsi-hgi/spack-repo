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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rnaEditr_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rnaEditr/rnaEditr_1.12.0.tar.gz"]

    version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="7b414f9324f243ee5ffb63061f89dde16a355b6325d6d906d904f38986f44a11")

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
