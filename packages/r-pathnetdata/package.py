# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathnetdata(RPackage):
	"""Experimental data for the PathNet package

	This package contains the data employed in the vignette of the PathNet package. These data belong to the following publication: PathNet: A tool for pathway analysis using topological information. Dutta B, Wallqvist A, and Reifman J., Source Code for Biology and Medicine 2012 Sep 24;7(1):10.
	"""
	
	bioc = "PathNetData"

	version("1.44.0", commit="cb2ce662fbbbb878448514b4093056aa8ae8c4c7")
	version("1.38.0", commit="165b1290c3dc13a468d9df74261ac5981fc236ef")

	depends_on("r@1.14:", type=("build", "run"))

