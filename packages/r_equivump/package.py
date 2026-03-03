# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REquivump(RPackage):
	"""Uniformly Most Powerful Invariant Tests of Equivalence

	Implementation of uniformly most powerful invariant equivalence
    tests for one- and two-sample problems (paired and unpaired) as described 
    in Wellek (2010, ISBN:978-1-4398-0818-4). Also one-sided alternatives 
    (non-inferiority and non-superiority tests) are supported. Basically a variant 
    of a t-test with (relaxed) null and alternative hypotheses exchanged.
	"""
	
	homepage = "https://github.com/thmild/equivUMP"
	cran = "equivUMP" 

	version("0.1.1", md5="836431e496a11bb61eaa674effb81793")

