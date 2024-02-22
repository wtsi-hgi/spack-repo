# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaq(RPackage):
	"""Multi-Armed Qini

	Evaluate treatment rules for costly and mutually exclusive treatment arms with Qini curves as proposed in Sverdrup, Wu, Athey, and Wager (2023) <arXiv:2306.11979>.
	"""
	
	homepage = "https://github.com/grf-labs/maq"
	cran = "maq" 

	version("0.3.1", md5="142544767bb66b1075b9bad525acbd41")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
