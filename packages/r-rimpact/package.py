# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRimpact(RPackage):
	"""Calculates Measures of Scholarly Impact

	The metrics() function calculates measures of scholarly impact. 
    These include conventional measures, such as the number of publications
    and the total citations to all publications, as well as modern and 
    robust metrics based on the vector of citations associated with each 
    publication, such as the h index and many of its variants or rivals.
    These methods are described in Ruscio et al. (2012) 
    <DOI: 10.1080/15366367.2012.711147>.
	"""
	
	cran = "RImpact" 

	version("1.0", md5="0b796064cc770129c813d9024f732ffa")

