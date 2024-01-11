# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RSctenifoldknk(RPackage):
	"""In-Silico Knockout Experiments from Single-Cell Gene Regulatory
Networks

	A workflow based on 'scTenifoldNet' to perform in-silico knockout experiments using single-cell RNA sequencing (scRNA-seq) data from wild-type (WT) control samples as input.  First, the package constructs a single-cell gene regulatory network (scGRN) and knocks out a target gene from the adjacency matrix of the WT scGRN by setting the gene’s outdegree edges to zero. Then, it compares the knocked out scGRN with the WT scGRN to identify differentially regulated genes, called virtual-knockout perturbed genes, which are used to assess the impact of the gene knockout and reveal the gene’s function in the analyzed cells.
	"""
	
	homepage = "https://github.com/cailab-tamu/scTenifoldKnk"
	cran = "scTenifoldKnk" 

	version("1.0.1", md5="c5ee56d67ab926d4ce9b6577ab81999d")

	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sctenifoldnet", type=("build", "run"))
	depends_on("r-testthat@2.1.0:", when="+r-testthat", type=("build", "run"))

	variant("r-testthat", default=False, description="Enable r-testthat support")
