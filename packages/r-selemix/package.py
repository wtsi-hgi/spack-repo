# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelemix(RPackage):
	"""Selective Editing via Mixture Models

	Detection of outliers and influential errors using a latent variable model. 
	"""
	
	cran = "SeleMix" 

	version("1.0.2", md5="1563ffdcc6b63f9a5c3a41fc0326f133")

	depends_on("r-mvtnorm", type=("build", "run"))
