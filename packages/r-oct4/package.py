# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROct4(RPackage):
	"""Conditional knockdown of OCT4 in mouse ESCs

	This package provides the output of running Salmon on a set of 12 RNA-seq samples from King & Klose, "The pioneer factor OCT4 requires the chromatin remodeller BRG1 to support gene regulatory element function in mouse embryonic stem cells", published in eLIFE, March 2017. For details on version numbers and how the samples were processed see the package vignette.
	"""
	
	bioc = "oct4" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/oct4_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/oct4/oct4_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="72a41a2bc6fbc0030d56d9f6599c83b408770f971d8e8482066a6ca5c5287bcd", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/oct4_1.18.0.tar.gz")


