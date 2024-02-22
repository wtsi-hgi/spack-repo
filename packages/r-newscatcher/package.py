# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNewscatcher(RPackage):
	"""Programmatically Collect Normalized News from (Almost) Any
Website

	Programmatically collect normalized news from
    (almost) any website. An 'R' clone of the
    <https://github.com/kotartemiy/newscatcher> 'Python' module.
	"""
	
	homepage = "https://github.com/discindo/newscatcheR/"
	cran = "newscatcheR" 

	version("0.1.2", md5="f313b10537d9cd20f714ee54715eed9b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tidyrss@2.0.2:", type=("build", "run"))
