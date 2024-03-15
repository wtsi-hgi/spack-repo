# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdrame(RPackage):
	"""FDR adjustments of Microarray Experiments (FDR-AME)

	This package contains two main functions. The first is fdr.ma which takes normalized expression data array, experimental design and computes adjusted p-values It returns the fdr adjusted p-values and plots, according to the methods described in (Reiner, Yekutieli and Benjamini 2002). The second, is fdr.gui() which creates a simple graphic user interface to access fdr.ma
	"""
	
	bioc = "fdrame" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/fdrame_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/fdrame/fdrame_1.74.0.tar.gz"]

	version("1.74.0", md5="d7fafba89f784f421a43b4b4d9a10000")

