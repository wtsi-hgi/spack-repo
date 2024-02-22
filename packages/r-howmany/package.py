# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHowmany(RPackage):
	"""A lower bound for the number of correct rejections

	When testing multiple hypotheses simultaneously, this
        package provides functionality to calculate a lower bound for
        the number of correct rejections (as a function of the number
        of rejected hypotheses), which holds simultaneously -with high
        probability- for all possible number of rejections.  As a
        special case, a lower bound for the total number of false null
        hypotheses can be inferred.  Dependent test statistics can be
        handled for multiple tests of associations. For independent
        test statistics, it is sufficient to provide a list of
        p-values.
	"""
	
	homepage = "http://www.stats.ox.ac.uk/~meinshau/"
	cran = "howmany" 

	version("0.3-1", md5="2a734431375a7214f6dc831ca004dc38")

