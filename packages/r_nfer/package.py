# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNfer(RPackage):
	"""Event Stream Abstraction using Interval Logic

	This is the R API for the 'nfer' formalism (<http://nfer.io/>).
    'nfer' was developed to specify event stream abstractions for spacecraft 
    telemetry such as the Mars Science Laboratory.  Users write rules using 
    a syntax that borrows heavily from Allen's Temporal Logic that, when 
    applied to an event stream, construct a hierarchy of temporal intervals 
    with data.  The R API supports loading rules from a file or mining them 
    from historical data.  Traces of events or pools of intervals are 
    provided as data frames.
	"""
	
	homepage = "http://nfer.io/"
	cran = "nfer" 

	version("1.1.3", md5="7dfe22dcde5fd1d5e64b9eec961abaae")

