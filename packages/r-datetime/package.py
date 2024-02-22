# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatetime(RPackage):
	"""Nominal Dates, Times, and Durations

	Provides methods for working with nominal dates, times, and 
 durations. Base R has sophisticated facilities for handling time, but these 
 can give unexpected results if, for example, timezone is not handled properly. 
 This package provides a more casual approach to support cases which 
 do not require rigorous treatment.  It systematically deconstructs the 
 concepts origin and timezone, and de-emphasizes the display of seconds. It 
 also converts among nominal durations such as seconds, hours, days, and weeks.
 See '?datetime' and '?duration' for examples. Adapted from 'metrumrg' 
 <http://r-forge.r-project.org/R/?group_id=1215>.
	"""
	
	cran = "datetime" 

	version("0.1.4", md5="cd91cab88ef9ac941afb1ca72561d7ef")

