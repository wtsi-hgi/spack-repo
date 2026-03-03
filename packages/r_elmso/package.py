# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElmso(RPackage):
	"""Implementation of the Efficient Large-Scale Online Display
Advertising Algorithm

	An implementation of the algorithm described in "Efficient Large-
    Scale Internet Media Selection Optimization for Online Display Advertising"
    by Paulson, Luo, and James (Journal of Marketing Research 2018; see URL below
    for journal text/citation and <http://faculty.marshall.usc.edu/gareth-james/Research/ELMSO.pdf>
    for a full-text version of the paper). The algorithm here is designed to 
    allocate budget across a set of online advertising opportunities using a 
    coordinate-descent approach, but it can be used in any resource-allocation 
    problem with a matrix of visitation (in the case of the paper, website page-
    views) and channels (in the paper, websites). The package contains allocation
    functions both in the presence of bidding, when allocation is dependent on 
    channel-specific cost curves, and when advertising costs are fixed at each channel.
	"""
	
	homepage = "<https://journals.sagepub.com/doi/abs/10.1509/jmr.15.0307>"
	cran = "ELMSO" 

	version("1.0.1", md5="37512e674085ba8cbbe9d453843a2df4")

	depends_on("r@3.4:", type=("build", "run"))
