# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChyper(RPackage):
	"""Functions for Conditional Hypergeometric Distributions

	An implementation of the probability mass function, cumulative density function, quantile function, random number generator, maximum likelihood estimator, and p-value generator from a conditional hypergeometric distribution: the distribution of how many items are in the overlap of all samples when samples of arbitrary size are each taken without replacement from populations of arbitrary size.
	"""
	
	cran = "chyper" 

	version("0.3.1", md5="cc99aa1146cfba5eae827c701ce2d916")

