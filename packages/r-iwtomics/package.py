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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/IWTomics_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/IWTomics/IWTomics_1.26.0.tar.gz"]

	version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="47aee4764390a177c055e23c14526e6fd4cc3b49f7151a92957e1c7af7bafc57")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
