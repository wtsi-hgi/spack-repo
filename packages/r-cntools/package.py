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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNTools_1.58.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CNTools/CNTools_1.58.0.tar.gz"]

    version("1.64.0", tag="RELEASE_3_21")
	version("1.58.0", sha256="e41de37c231a5688e3b0e65b48a7caaa452d06e44bdf82cd325f48bcf23664cb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
