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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DelayedDataFrame_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DelayedDataFrame/DelayedDataFrame_1.18.0.tar.gz"]

	version("1.18.0", md5="dd12410d16a2e6cf7bb022d2aa334bf7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-s4vectors@0.23.19:", type=("build", "run"))
	depends_on("r-delayedarray@0.7.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
