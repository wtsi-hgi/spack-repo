# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignedBackbones(RPackage):
	"""Extract the Signed Backbones of Weighted Networks

	Extract the signed backbones of intrinsically dense weighted networks based on the significance filter and vigor filter as described in the following paper. Please cite it if you find this software useful in your work.	
	Furkan Gursoy and Bertan Badur. "Extracting the signed backbone of intrinsically dense weighted networks." Journal of Complex Networks. <arXiv:2012.05216>.
	"""
	
	cran = "signed.backbones" 

	version("0.91.5", md5="c1dbdf4a643d0f2b5e07e276e3ae9eae")

	depends_on("r-reshape2", type=("build", "run"))
