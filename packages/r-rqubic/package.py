# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqubic(RPackage):
	"""Qualitative biclustering algorithm for expression data analysis in R

	This package implements the QUBIC algorithm introduced by Li et al. for the qualitative biclustering with gene expression data.
	"""
	
	bioc = "rqubic" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rqubic_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rqubic/rqubic_1.48.0.tar.gz"]

    version("1.54.0", tag="RELEASE_3_21")
	version("1.48.0", sha256="3efd6ae688c563f6c290b4caad696c968bd2a9b7b30c72a2f84d525016721138")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biclust", type=("build", "run"))
