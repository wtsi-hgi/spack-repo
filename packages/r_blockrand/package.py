# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlockrand(RPackage):
	"""Randomization for Block Random Clinical Trials

	Create randomizations for block random clinical trials.  Can also produce a pdf file of randomization cards.
	"""
	
	cran = "blockrand" 

	version("1.5", md5="33d7c40ca94bacc8bcecfcfbb5692f4f")

