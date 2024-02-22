# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhphybrid(RPackage):
	"""AHP Hybrid Method

	The AHP method (Analytic Hierarchy Process) is a multi-criteria decision-making method addressing
             choice and outranking problems. The method enables to perform the analysis of alternatives in each
             type of criterion and then provides a global performance of each alternative in the decision context.
             The main difference of this package is the possibility of evaluating the alternatives using quantitative
             data, by numerical representation, and qualitative data, using the Saaty scale, providing preference
             relation between variables by a pairwise evaluation.
	"""
	
	cran = "AHPhybrid" 

	version("0.1.0", md5="e4f763be46e995aa7e56d0570d7785a0")

