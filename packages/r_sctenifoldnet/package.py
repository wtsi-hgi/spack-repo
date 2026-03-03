# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSctenifoldnet(RPackage):
	"""Construct and Compare scGRN from Single-Cell Transcriptomic Data

	A workflow based on machine learning methods to construct and compare single-cell gene regulatory networks (scGRN) using single-cell RNA-seq (scRNA-seq) data collected from different conditions. Uses principal component regression, tensor decomposition, and manifold alignment, to accurately identify even subtly shifted gene expression programs. See <doi:10.1016/j.patter.2020.100139> for more details.
	"""
	
	homepage = "https://github.com/cailab-tamu/scTenifoldNet"
	cran = "scTenifoldNet" 

	version("1.3", md5="7bf583c867b0254d0ab062f6ba3b60ef")

	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
