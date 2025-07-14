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

	version("1.80.0", commit="2d21a443ea14b11196c299ba3e0ce892d25e1f3c")
	version("1.74.0", commit="3b67352d235430e4182293147ca511a5e2f3b4cd")

