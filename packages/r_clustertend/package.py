# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustertend(RPackage):
	"""Check the Clustering Tendency

	Calculate some statistics aiming to help analyzing the clustering tendency of given data. In the first version, Hopkins statistic is implemented. See Hopkins and Skellam (1954) <doi:10.1093/oxfordjournals.aob.a083391>.
	"""
	
	cran = "clustertend" 

	version("1.7", md5="a9f138d997707c0351925fc7ea525439")

