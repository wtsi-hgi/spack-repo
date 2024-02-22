# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultigroupsequential(RPackage):
	"""Group-Sequential Procedures with Multiple Hypotheses

	It is often challenging to strongly control the family-wise type-1 error rate in the group-sequential trials with multiple endpoints (hypotheses). The inflation of type-1 error rate comes from two sources (S1) repeated testing individual hypothesis and (S2) simultaneous testing multiple hypotheses. The 'MultiGroupSequential' package is intended to help researchers to tackle this challenge. The procedures provided include the sequential procedures described in Luo and Quan (2023) <doi:10.1080/19466315.2023.2191989> and the graphical procedure proposed by Maurer and Bretz (2013) <doi:10.1080/19466315.2013.807748>. Luo and Quan (2013) describes three procedures, and the functions to implement these procedures are (1) seqgspgx() implements a sequential graphical procedure based on the group-sequential p-values; (2) seqgsphh() implements a sequential Hochberg/Hommel procedure based on the group-sequential p-values; and (3) seqqvalhh() implements a sequential Hochberg/Hommel procedure based on the q-values. In addition, seqmbgx() implements the sequential graphical procedure described in Maurer and Bretz (2013).
	"""
	
	cran = "MultiGroupSequential" 

	version("1.1.0", md5="4cda66ca315bcc99c91aaa7d017704b3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-openmx", type=("build", "run"))
	depends_on("r-hommel", type=("build", "run"))
