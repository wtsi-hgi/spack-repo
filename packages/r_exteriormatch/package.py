# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExteriormatch(RPackage):
	"""Constructs the Exterior Match from Two Matched Control Groups

	If one treated group is matched to one control reservoir in two different ways to produce two sets of treated-control matched pairs, then the two control groups may be entwined, in the sense that some control individuals are in both control groups.  The exterior match is used to compare the two control groups.
	"""
	
	cran = "exteriorMatch" 

	version("1.0.0", md5="4d39a2e567cf0d67d7fd05b854e5df90")

