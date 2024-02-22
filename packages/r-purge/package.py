# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPurge(RPackage):
	"""Purge Training Data from Models

	Enables the removal of training data from fitted R models while
    retaining predict functionality. The purged models are more portable as their
    memory footprints do not scale with the training sample size.
	"""
	
	cran = "purge" 

	version("0.2.1", md5="d0add15a997b5447d3b3c0a21ec01a1b")

