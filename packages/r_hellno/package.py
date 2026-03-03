# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHellno(RPackage):
	"""Providing 'stringsAsFactors=FALSE' Variants of 'data.frame()'
and 'as.data.frame()'

	Base R's default setting for 'stringsAsFactors' within
    'data.frame()' and 'as.data.frame()' is supposedly the most often complained
    about piece of code in the R infrastructure. The 'hellno' package provides
    an explicit solution without changing R itself or having to mess around with
    options. It tries to solve this problem by providing alternative
    'data.frame()' and 'as.data.frame()' functions that are in fact simple
    wrappers around base R's 'data.frame()' and 'as.data.frame()' with
    'stringsAsFactors' option set to 'HELLNO' ( which in turn equals FALSE )
    by default.
	"""
	
	homepage = "https://github.com/petermeissner/hellno"
	cran = "hellno" 

	version("0.0.1", md5="eaa5245cf0626cdad1640950e2aeed62")

