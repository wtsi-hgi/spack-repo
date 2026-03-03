# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIss(RPackage):
	"""Isotonic Subgroup Selection

	Methodology for subgroup selection in the context of isotonic regression including methods for sub-Gaussian errors, classification, homoscedastic Gaussian errors and quantile regression. See the documentation of ISS(). Details can be found in the paper by Müller, Reeve, Cannings and Samworth (2023) <arXiv:2305.04852v2>.
	"""
	
	cran = "ISS" 

	version("1.0.0", md5="d0c213d2363809b46236a062f1e094ae")

	depends_on("r-rdpack@0.7:", type=("build", "run"))
