# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndexnumber(RPackage):
	"""Index Numbers in Social Sciences

	We provide an R tool for teaching in Social Sciences. It allows the computation of index numbers. It is a measure of the evolution of a fixed magnitude for only a product of for several products. It is very useful in Social Sciences. Among others, we obtain simple index numbers (in chain or in serie), index numbers for not only a product or weighted index numbers as the Laspeyres index (Laspeyres, 1864), the Paasche index (Paasche, 1874) or the Fisher index (Lapedes, 1978).
	"""
	
	cran = "IndexNumber" 

	version("1.3.2", md5="96e0463a099b12042224ee949ee24475")

