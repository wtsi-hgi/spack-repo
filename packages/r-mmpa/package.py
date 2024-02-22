# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmpa(RPackage):
	"""Implementation of Marker-Assisted Mini-Pooling with Algorithm

	To determine the number of quantitative assays needed for a sample 
    of data using pooled testing methods, which include mini-pooling (MP), MP 
    with algorithm (MPA), and marker-assisted MPA (mMPA). To estimate the number 
    of assays needed, the package also provides a tool to conduct Monte Carlo (MC) 
    to simulate different orders in which the sample would be collected to form pools. 
    Using MC avoids the dependence of the estimated number of assays on any specific 
    ordering of the samples to form pools.
	"""
	
	cran = "mMPA" 

	version("1.2.0", md5="d2aca0ddaf5df2fabf8790225aa85cb1")

