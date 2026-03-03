# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBimodalindex(RPackage):
	"""The Bimodality Index

	Defines the functions used to compute the
  bimodal index as defined by Wang et al. (2009)
  <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2730180/>,
  <doi:10.4137/CIN.S2846>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "BimodalIndex" 

	version("1.1.9", md5="e7a8a6e41e98dc536c5785a16d1db8fb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-oompabase@3.0.1:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
