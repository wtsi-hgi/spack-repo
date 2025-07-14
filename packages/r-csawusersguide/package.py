# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsawusersguide(RPackage):
	"""csaw User's Guide

	A user's guide for the csaw package for detecting differentially bound regions in ChIP-seq data. Describes how to read in BAM files to obtain a per-window count matrix, filtering to obtain high-abundance windows of interest, normalization of sample-specific biases, testing for differential binding, consolidation of per-window results to obtain per-region statistics, and annotation and visualization of the DB results.
	"""
	
	bioc = "csawUsersGuide" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/csawUsersGuide_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/csawUsersGuide/csawUsersGuide_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="e69cdfae2b84065235290b25b99d715408b2823ea2d640671a4fa72683fed919")


