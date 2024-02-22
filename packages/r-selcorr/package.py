# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelcorr(RPackage):
	"""Post-Selection Inference for Generalized Linear Models

	Calculates (unconditional) post-selection confidence intervals
    and p-values for the coefficients of (generalized) linear models.
	"""
	
	cran = "selcorr" 

	version("1.0", md5="b62b2a7000ecda204b41bf26f0b5aef5")

	depends_on("r-mass", type=("build", "run"))
