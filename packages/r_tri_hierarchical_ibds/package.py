# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriHierarchicalIbds(RPackage):
	"""Tri-Hierarchical IBDs (Tri- Hierarchical Incomplete Block
Designs)

	Tri-hierarchical incomplete block design is defined as an arrangement of v  treatments each replicated r  times in a three system of blocks if, each block of the first system contains m_1 blocks of second system and each block of the second system contains m_2 blocks of the third system. Ignoring the first and second system of blocks, it leaves an incomplete block design with b_3 blocks of size k_3i units; ignoring first and third system of blocks, it leaves an incomplete block design with b_2 blocks each of size k_2i units and ignoring the second and third system of blocks, it leaves an incomplete block design with b_1 blocks each of size k_1 units. For dealing with experimental circumstances where there are three nested sources of variation, a tri-hierarchical incomplete block design can be adopted. Tri - hierarchical incomplete block designs can find application potential in obtaining mating-environmental designs for breeding trials. To know more about nested block designs one can refer Preece (1967) <doi:10.1093/biomet/54.3-4.479>. This package includes series1(), series2(), series3() and series4() functions. This package generates tri-hierarchical designs with six component designs under certain parameter restrictions.
	"""
	
	cran = "Tri.Hierarchical.IBDs" 

	version("1.0.0", md5="bc602aef3198a29516416c7ef703981e")

