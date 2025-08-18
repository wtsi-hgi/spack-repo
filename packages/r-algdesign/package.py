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

	def patch(self):
		# Align a few C prototypes with their definitions for newer compilers/R >= 4.5
		# BacksolveT: third arg is int in definition
		filter_file(
			r"void\s+BacksolveT\(double\s*\*matrixXY,\s*int\s*nColumns,\s*bool\s*scaled\);",
			r"void BacksolveT(double *matrixXY,int nColumns,int scaled);",
			"src/FederovOpt.c",
		)

		# FederovOptimize: last parameter is int* error in definition
		filter_file(
			r"bool\s*\*error\)\s*;",
			r"int *error);",
			"src/FederovOpt.c",
		)

		# ProgDealloc prototype uses int* rather than bool*
		filter_file(r"bool\s*\*designFlag", r"int *designFlag", "src/FederovOpt.c")
		filter_file(r"bool\s*\*ttrows", r"int *ttrows", "src/FederovOpt.c")

		# Avoid undefined symbol Free at link time; map to free
		filter_file(r"\bFree\(", r"free(", "src/FederovOpt.c")

		# In OptBlock.c the ProgAllocate prototype takes an int criterion in definition
		# Normalize the prototype line
		filter_file(r"bool\s+criterion", r"int criterion", "src/OptBlock.c")

