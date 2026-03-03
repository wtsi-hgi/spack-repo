# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphon(RPackage):
	"""A Collection of Graphon Estimation Methods

	Provides a not-so-comprehensive list of methods for estimating graphon,
    a symmetric measurable function, from a single or multiple of observed networks. 
    For a detailed introduction on graphon and popular estimation techniques, 
    see the paper by Orbanz, P. and Roy, D.M.(2014) <doi:10.1109/TPAMI.2014.2334607>.
    It also contains several auxiliary functions for generating sample networks
    using various network models and graphons.
	"""
	
	cran = "graphon" 

	version("0.3.5", md5="9687b1422f786646acebb5e864c40065")

	depends_on("r-roptspace", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
