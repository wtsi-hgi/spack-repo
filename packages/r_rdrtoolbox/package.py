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

	version("1.52.0", md5="4b0e59a1ea48dd51e11d8d18666cf2d4")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
