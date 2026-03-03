# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeaksegdp(RPackage):
	"""Dynamic Programming Algorithm for Peak Detection in ChIP-Seq
Data

	A quadratic time dynamic programming algorithm
 can be used to compute an approximate solution to the problem of
 finding the most likely changepoints
 with respect to the Poisson likelihood, subject
 to a constraint on the number of segments, and the changes which must
 alternate: up, down, up, down, etc. For more info read
 <http://proceedings.mlr.press/v37/hocking15.html>
 "PeakSeg: constrained optimal segmentation and supervised penalty learning
 for peak detection in count data" by TD Hocking et al,
 proceedings of ICML2015.
	"""
	
	homepage = "https://github.com/tdhock/PeakSegDP"
	cran = "PeakSegDP" 

	version("2024.1.24", md5="6e65d0ed5347a01dbd3edec4f79d66c9")

	depends_on("r@2.10:", type=("build", "run"))
