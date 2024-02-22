# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchdata(RPackage):
	"""Example Datasets from Archaeological Research

	The archdata package provides several types of data that are typically used in archaeological research. It provides all of the data sets used in "Quantitative Methods in Archaeology Using R" by David L Carlson, one of the Cambridge Manuals in Archaeology.
	"""
	
	cran = "archdata" 

	version("1.2-1", md5="521e8c471b0eab62fc92dd6d500c4de5")

