# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSars(RPackage):
	"""Fit and Compare Species-Area Relationship Models Using
Multimodel Inference

	Implements the basic elements of the multi-model
    inference paradigm for up to twenty species-area relationship models (SAR), using simple
    R list-objects and functions, as in Triantis et al. 2012 <DOI:10.1111/j.1365-2699.2011.02652.x>.
    The package is scalable and users can easily create their own model and data objects. Additional
    SAR related functions are provided.
	"""
	
	homepage = "https://github.com/txm676/sars"
	cran = "sars" 

	version("1.3.6", md5="d51131876f83eb52d4d45f6175eb313f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-aiccmodavg", type=("build", "run"))
