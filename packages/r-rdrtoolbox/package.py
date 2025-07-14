# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdrtoolbox(RPackage):
	"""A package for nonlinear dimension reduction with Isomap and LLE.

	A package for nonlinear dimension reduction using the Isomap and LLE algorithm. It also includes a routine for computing the Davis-Bouldin-Index for cluster validation, a plotting tool and a data generator for microarray gene expression data and for the Swiss Roll dataset.
	"""
	
	bioc = "RDRToolbox" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RDRToolbox_1.52.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RDRToolbox/RDRToolbox_1.52.0.tar.gz"]

    version("1.58.0", tag="RELEASE_3_21")
	version("1.52.0", sha256="c9937a8c609df4f40bb3567a713cd099ba4ea90972c5a4775e83958802042acc")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
