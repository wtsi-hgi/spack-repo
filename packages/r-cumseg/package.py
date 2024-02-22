# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCumseg(RPackage):
	"""Change Point Detection in Genomic Sequences

	Estimation of number and location of change points in
        mean-shift (piecewise constant) models. Particularly useful (but not confined) to
        model genomic sequences of continuous measurements.
	"""
	
	cran = "cumSeg" 

	version("1.3", md5="1c85af9c8ba93b16dc04fac52eb43eae")

	depends_on("r-lars", type=("build", "run"))
