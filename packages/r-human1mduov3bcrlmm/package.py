# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuman1mduov3bcrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina 1M Duo arrays using the 'crlmm' package.
	"""
	
	bioc = "human1mduov3bCrlmm" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/human1mduov3bCrlmm_1.0.4.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/human1mduov3bCrlmm/human1mduov3bCrlmm_1.0.4.tar.gz"]

	version("1.0.4", md5="0ff9f1e8bcc6348d6777bbb982ae0325")


	# annotation