# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipseqdb(RPackage):
	"""A Bioconductor Workflow to Detect Differential Binding in ChIP-seq Data

	Describes a computational workflow for performing a DB analysis with sliding windows. The aim is to facilitate the practical implementation of window-based DB analyses by providing detailed code and expected output. The workflow described here applies to any ChIP-seq experiment with multiple experimental conditions and multiple biological samples in one or more of the conditions. It detects and summarizes DB regions between conditions in a de novo manner, i.e., without making any prior assumptions about the location or width of bound regions. Detected regions are then annotated according to their proximity to genes.
	"""
	
	homepage = "https://www.bioconductor.org/help/workflows/chipseqDB/"
	bioc = "chipseqDB" 
	urls = ["https://www.bioconductor.org/packages/release/workflows/src/contrib/chipseqDB_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/workflows/src/contrib/Archive/chipseqDB/chipseqDB_1.26.0.tar.gz"]

	version("1.26.0", md5="5337080bfb457f5bb9754b4a5a2a1c88")


	# workflow