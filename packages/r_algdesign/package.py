# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlgdesign(RPackage):
	"""Algorithmic Experimental Design

	Algorithmic experimental designs. Calculates exact and
        approximate theory experimental designs for D,A, and I
        criteria. Very large designs may be created. Experimental
        designs may be blocked or blocked designs created from a
        candidate list, using several criteria.  The blocking can be
        done when whole and within plot factors interact.
	"""
	
	homepage = "https://github.com/jvbraun/AlgDesign"
	cran = "AlgDesign" 

	version("1.2.1", md5="fd2c7ba6d0cc0b438dd530c4a25c4017")

