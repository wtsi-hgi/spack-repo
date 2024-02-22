# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDodge(RPackage):
	"""Acceptance Sampling Ideas Originated by H.F. Dodge

	A variety of sampling plans are able to be compared using evaluations of their operating characteristics (OC), average outgoing quality (OQ), average total inspection (ATI) etc.
	"""
	
	homepage = "https://github.com/ajrgodfrey/Dodge"
	cran = "Dodge" 

	version("0.9-2", md5="932af5b821afbd75bb10d3b60e8bb3c3")

	depends_on("r@2.14:", type=("build", "run"))
