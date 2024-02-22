# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSknn(RPackage):
	"""A Super K-Nearest Neighbor (SKNN) Classification Algorithm

	It's a Super K-Nearest Neighbor classification method with using kernel density to describe weight of the distance between a training observation and the testing sample. 
	"""
	
	cran = "SKNN" 

	version("3.1", md5="2f863e4d298a47e73f5b47fcfd9abd21")

