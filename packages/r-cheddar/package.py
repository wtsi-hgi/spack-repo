# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheddar(RPackage):
	"""Analysis and Visualisation of Ecological Communities

	Provides a flexible, extendable representation of an ecological community and a range of functions for analysis and visualisation, focusing on food web, body mass and numerical abundance data. Allows inter-web comparisons such as examining changes in community structure over environmental, temporal or spatial gradients.
	"""
	
	homepage = "https://github.com/quicklizard99/cheddar/"
	cran = "cheddar" 

	version("0.1-638", md5="d7a318899c2d311d8721d856c7c12d71")

