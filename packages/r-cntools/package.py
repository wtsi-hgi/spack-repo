# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCntools(RPackage):
	"""Convert segment data into a region by sample matrix to allow for other high level computational analyses.

	This package provides tools to convert the output of segmentation analysis using DNAcopy to a matrix structure with overlapping segments as rows and samples as columns so that other computational analyses can be applied to segmented data
	"""
	
	bioc = "CNTools" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CNTools_1.58.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CNTools/CNTools_1.58.0.tar.gz"]

	version("1.58.0", md5="e3ce148937711a84dadf67b5f09c5373")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
