# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisparityfilter(RPackage):
	"""Disparity Filter Algorithm for Weighted Networks

	The disparity filter algorithm is a network reduction technique to
    identify the 'backbone' structure of a weighted network without destroying
    its multi-scale nature. The algorithm is documented in M. Angeles Serrano,
    Marian Boguna and Alessandro Vespignani in "Extracting the multiscale
    backbone of complex weighted networks", Proceedings of the National Academy
    of Sciences 106 (16), 2009. This implementation of the algorithm supports
    both directed and undirected networks.
	"""
	
	homepage = "https://github.com/alessandrobessi/disparityfilter"
	cran = "disparityfilter" 

	version("2.2.3", md5="74dc155376ecb19de3b4989256eb9b9f")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
