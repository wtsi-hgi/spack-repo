# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsat(RPackage):
	"""OSAT: Optimal Sample Assignment Tool

	A sizable genomics study such as microarray often involves the use of multiple batches (groups) of experiment due to practical complication. To minimize batch effects, a careful experiment design should ensure the even distribution of biological groups and confounding factors across batches. OSAT (Optimal Sample Assignment Tool) is developed to facilitate the allocation of collected samples to different batches. With minimum steps, it produces setup that optimizes the even distribution of samples in groups of biological interest into different batches, reducing the confounding or correlation between batches and the biological variables of interest. It can also optimize the even distribution of confounding factors across batches. Our tool can handle challenging instances where incomplete and unbalanced sample collections are involved as well as ideal balanced RCBD. OSAT provides a number of predefined layout for some of the most commonly used genomics platform. Related paper can be find at http://www.biomedcentral.com/1471-2164/13/689 .
	"""
	
	homepage = "http://www.biomedcentral.com/1471-2164/13/689"
	bioc = "OSAT"

	version("1.56.0", commit="2a6f05f1e91f5331848c8070100fa32771124838")
	version("1.50.0", commit="24ffc7d05ef9b7e5295342519bdfc13df9c2ffa8")

