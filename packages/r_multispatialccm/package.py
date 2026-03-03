# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultispatialccm(RPackage):
	"""Multispatial Convergent Cross Mapping

	The multispatial convergent cross mapping algorithm can be used as a test for causal associations between pairs of processes represented by time series. This is a combination of convergent cross mapping (CCM), described in Sugihara et al., 2012, Science, 338, 496-500, and dew-drop regression, described in Hsieh et al., 2008, American Naturalist, 171, 71–80. The algorithm allows CCM to be implemented on data that are not from a single long time series. Instead, data can come from many short time series, which are stitched together using bootstrapping.
	"""
	
	cran = "multispatialCCM" 

	version("1.3", md5="702694fe275b9936421c01f2760f13d6")

	depends_on("r@3.0.2:", type=("build", "run"))
