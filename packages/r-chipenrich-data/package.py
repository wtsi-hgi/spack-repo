# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipenrichData(RPackage):
	"""Companion package to chipenrich

	Supporting data for the chipenrich package. Includes pre-defined gene sets, gene locus definitions, and mappability estimates.
	"""
	
	bioc = "chipenrich.data" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/chipenrich.data_2.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/chipenrich.data/chipenrich.data_2.26.0.tar.gz"]

	version("2.26.0", md5="4918da98125fee82afaeee84930051a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

	# experiment