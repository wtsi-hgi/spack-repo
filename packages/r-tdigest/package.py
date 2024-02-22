# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdigest(RPackage):
	"""Wicked Fast, Accurate Quantiles Using t-Digests

	The t-Digest construction algorithm, by 
    Dunning et al., (2019) <arXiv:1902.04023v1>, uses a variant of 1-dimensional 
    k-means clustering to produce a very compact data structure that allows 
    accurate estimation of quantiles. This t-Digest data structure can be used 
    to estimate quantiles, compute other rank statistics or even to estimate 
    related measures like trimmed means. The advantage of the t-Digest over 
    previous digests for this purpose is that the t-Digest handles data with 
    full floating point resolution. The accuracy of quantile estimates produced 
    by t-Digests can be orders of magnitude more accurate than those produced 
    by previous digest algorithms. Methods are provided to create and update 
    t-Digests and retrieve quantiles from the accumulated distributions.
	"""
	
	homepage = "https://git.sr.ht/~hrbrmstr/tdigest"
	cran = "tdigest" 

	version("0.4.1", md5="ae5f6b4d96071a4731a36fe654708542")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
