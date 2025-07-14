# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMofadata(RPackage):
	"""Data package for Multi-Omics Factor Analysis (MOFA)

	A collection of datasets to accompany the R package MOFA and illustrate running and analysing MOFA models.
	"""
	
	bioc = "MOFAdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MOFAdata_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MOFAdata/MOFAdata_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="c1e32c68192a91e9174f345cfbc97b73879594b0182fd51642ef2047db4885de")

	depends_on("r@3.5:", type=("build", "run"))

