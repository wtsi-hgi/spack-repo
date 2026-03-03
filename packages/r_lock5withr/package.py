# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLock5withr(RPackage):
	"""Datasets for 'Statistics: Unlocking the Power of Data'

	Data sets and other utilities for 
    'Statistics: Unlocking the Power of Data'
    by Lock, Lock, Lock, Lock and Lock 
    (ISBN : 978-0-470-60187-7, http://lock5stat.com/).
	"""
	
	cran = "Lock5withR" 

	version("1.2.2", md5="ea9465d62485b35a26fe4bb8f867bf74")

	depends_on("r@2.10:", type=("build", "run"))
