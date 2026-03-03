# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlopeop(RPackage):
	"""Change-in-Slope OP Algorithm with a Finite Number of States

	Optimal partitioning algorithm for change-in-slope problem with continuity constraint and a finite number of states. Some constraints can be enforced in the inference: isotonic, unimodal or smoothing. With the function slopeSN() (segment neighborhood) the number of segments to infer is fixed by the user and does not depend on a penalty value.
	"""
	
	cran = "slopeOP" 

	version("1.0.1", md5="fb2c3589b7a0a89fe5f5c26b87f2ab2a")

	depends_on("r-rcpp", type=("build", "run"))
