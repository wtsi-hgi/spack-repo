# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIwtomics(RPackage):
	"""Interval-Wise Testing for Omics Data

	Implementation of the Interval-Wise Testing (IWT) for omics data. This inferential procedure tests for differences in "Omics" data between two groups of genomic regions (or between a group of genomic regions and a reference center of symmetry), and does not require fixing location and scale at the outset.
	"""
	
	bioc = "IWTomics" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/IWTomics_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/IWTomics/IWTomics_1.26.0.tar.gz"]

	version("1.26.0", md5="f571644700ff672c2ac90aa49b611158")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
