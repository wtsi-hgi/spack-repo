# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTablehc(RPackage):
	"""Higher Criticism Test of Two Frequency Counts Tables

	Higher Criticism (HC) test between two frequency tables. Test is based on an adaptation of the Tukey-Donoho-Jin HC statistic to testing frequency tables described in Kipnis (2019) <arXiv:1911.01208>. 
	"""
	
	cran = "TableHC" 

	version("0.1.2", md5="3c94e4188adc73c6f69dd8adfc14670d")

