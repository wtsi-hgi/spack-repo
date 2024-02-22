# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbs2ploidy(RPackage):
	"""Inference of Ploidy from (Genotyping-by-Sequencing) GBS Data

	Functions for inference of ploidy from (Genotyping-by-sequencing) GBS data, including a function to infer allelic ratios and allelic proportions in a Bayesian framework. 
	"""
	
	cran = "gbs2ploidy" 

	version("1.0", md5="4fbd859a813d612955f5686e568a3e85")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
