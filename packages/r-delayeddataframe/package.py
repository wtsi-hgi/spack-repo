# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDelayeddataframe(RPackage):
	"""Delayed operation on DataFrame using standard DataFrame metaphor

	Based on the standard DataFrame metaphor, we are trying to implement the feature of delayed operation on the DelayedDataFrame, with a slot of lazyIndex, which saves the mapping indexes for each column of DelayedDataFrame. Methods like show, validity check, [/[[ subsetting, rbind/cbind are implemented for DelayedDataFrame to be operated around lazyIndex. The listData slot stays untouched until a realization call e.g., DataFrame constructor OR as.list() is invoked.
	"""
	
	homepage = "https://github.com/Bioconductor/DelayedDataFrame"
	bioc = "DelayedDataFrame" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DelayedDataFrame_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DelayedDataFrame/DelayedDataFrame_1.18.0.tar.gz"]

	version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="cb76488971d7e26d6df500669504ec70757fee265d0f258d42c0e33ea4b8e143")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-s4vectors@0.23.19:", type=("build", "run"))
	depends_on("r-delayedarray@0.7.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
