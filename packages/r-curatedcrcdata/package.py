# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedcrcdata(RPackage):
	"""Colorectal Cancer Gene Expression Analysis

	The curatedCRC package provides relevant functions and data for gene expression analysis in patients with colorectal cancer.
	"""
	
	homepage = "https://bitbucket.org/biobakery/curatedcrcdata"
	bioc = "curatedCRCData"

	version("2.40.0", commit="c51a05bb4287d17700656fa33194e4a7d1de3b5b")
	version("2.34.0", commit="3df2048e8439fca7d7dd43289475512e05a69faf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

