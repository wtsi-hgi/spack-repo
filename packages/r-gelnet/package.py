# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGelnet(RPackage):
	"""Generalized Elastic Nets

	Implements several extensions of the elastic net regularization
    scheme. These extensions include individual feature penalties for the L1 term,
    feature-feature penalties for the L2 term, as well as translation coefficients
    for the latter.
	"""
	
	cran = "gelnet" 

	version("1.2.1", md5="b48a5314d49876eff323d083bf38f21d")

	depends_on("r@3.1:", type=("build", "run"))
