# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNets(RPackage):
	"""Network Estimation for Time Series

	Sparse VAR estimation based on LASSO.
	"""
	
	homepage = "https://github.com/ctbrownlees/R-Package-nets"
	cran = "nets" 

	version("0.9.1", md5="e965b315b003a4f17a633cbabf854e33")

	depends_on("r-igraph", type=("build", "run"))
