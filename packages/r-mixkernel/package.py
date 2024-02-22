# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixkernel(RPackage):
	"""Omics Data Integration Using Kernel Methods

	Kernel-based methods are powerful methods for integrating 
    heterogeneous types of data. mixKernel aims at providing methods to combine
    kernel for unsupervised exploratory analysis. Different solutions are 
    provided to compute a meta-kernel, in a consensus way or in a way that 
    best preserves the original topology of the data. mixKernel also integrates
    kernel PCA to visualize similarities between samples in a non linear space
    and from the multiple source point of view 
    <doi:10.1093/bioinformatics/btx682>. A method to select (as well as 
    funtions to display) important variables is also provided 
    <doi:10.1093/nargab/lqac014>.
	"""
	
	homepage = "http://mixkernel.clementine.wf"
	cran = "mixKernel" 

	version("0.9-1", md5="fec0b11e02762ebb9256c2ffcf2c6110")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reticulate@1.14:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-ldrtools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
