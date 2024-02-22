# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffee(RPackage):
	"""Fast and Scalable Learning of Sparse Changes in High-Dimensional
Gaussian Graphical Model Structure

	This is an R implementation of Fast and Scalable Learning of Sparse Changes in High-Dimensional Gaussian Graphical Model Structure (DIFFEE). The DIFFEE algorithm can be used to fast estimate the differential network between two related datasets. For instance, it can identify differential gene network from datasets of case and control. By performing data-driven network inference from two high-dimensional data sets, this tool can help users effectively translate two aggregated data blocks into knowledge of the changes among entities between two Gaussian Graphical Model. Please run demo(diffeeDemo) to learn the basic functions provided by this package. For further details, please read the original paper: Beilun Wang, Arshdeep Sekhon, Yanjun Qi (2018) <arXiv:1710.11223>.
	"""
	
	homepage = "https://github.com/QData/DIFFEE"
	cran = "diffee" 

	version("1.1.0", md5="d213fe37867e58890fb23ae9e735ad6c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
