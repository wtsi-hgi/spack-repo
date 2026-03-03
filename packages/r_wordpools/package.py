# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordpools(RPackage):
	"""Word Pools Used in Studies of Learning and Memory

	Collects several classical word pools used most often
    to provide lists of words in psychological studies of learning and memory. It
    provides a simple function, 'pickList' for selecting random samples of words
    within given ranges.
	"""
	
	cran = "WordPools" 

	version("1.2.0", md5="af6b4a46a00701a9268f2056903134cf")

	depends_on("r@3.5:", type=("build", "run"))
