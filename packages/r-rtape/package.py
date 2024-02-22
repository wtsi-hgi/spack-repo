# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtape(RPackage):
	"""Manage and manipulate large collections of R objects stored as
tape-like files

	Storing huge data in RData format causes problems because
        of the necessity to load the whole file to the memory in order
        to access and manipulate objects inside such file; rtape is a
        simple solution to this problem. The package contains several
        wrappers of R built-in serialize/unserialize mechanism allowing
        user to quickly append objects to a tape-like file and later
        iterate over them requiring only one copy of each stored object
        to reside in memory a time.
	"""
	
	homepage = "http://mbq.me/rtape"
	cran = "rtape" 

	version("2.2", md5="18c33bb208b0594a49e41cd53fe18d9b")

