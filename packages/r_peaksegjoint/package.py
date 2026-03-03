# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeaksegjoint(RPackage):
	"""Joint Peak Detection in Several ChIP-Seq Samples

	Jointly segment several ChIP-seq samples to find the peaks 
 which are the same and different across samples. The fast approximate
 maximum Poisson likelihood algorithm is described in
 "PeakSegJoint: fast supervised peak detection via joint segmentation
 of multiple count data samples"
 <arXiv:1506.01286> by TD Hocking and G Bourque.
	"""
	
	homepage = "https://github.com/tdhock/PeakSegJoint"
	cran = "PeakSegJoint" 

	version("2024.1.24", md5="31326d0709c0a0ae83fb726f7eb72592")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-peakerror", type=("build", "run"))
	depends_on("r-penaltylearning", type=("build", "run"))
