# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuman550v3bcrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina 550k arrays using the 'crlmm' package.
	"""
	
	bioc = "human550v3bCrlmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/human550v3bCrlmm_1.0.4.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/human550v3bCrlmm/human550v3bCrlmm_1.0.4.tar.gz"]

	version("1.0.4", md5="20e6b008fab5e1084354c87ad50d18a8")


