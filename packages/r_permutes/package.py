# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermutes(RPackage):
	"""Permutation Tests for Time Series Data

	Helps you determine the analysis window to use when analyzing densely-sampled
    time-series data, such as EEG data, using permutation testing (Maris & Oostenveld, 2007)
    <doi:10.1016/j.jneumeth.2007.03.024>. These permutation tests can help identify the timepoints
    where significance of an effect begins and ends, and the results can be plotted in various
    types of heatmap for reporting. Mixed-effects models are supported using an implementation of
    the approach by Lee & Braun (2012) <doi:10.1111/j.1541-0420.2011.01675.x>.
	"""
	
	cran = "permutes" 

	version("2.8", md5="a5833cd890a2086c825177aec4f63aa4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
