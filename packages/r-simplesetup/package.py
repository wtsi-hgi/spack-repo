# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplesetup(RPackage):
	"""Set Up R Source Code Files for Use on Multiple Machines

	When working across multiple machines and, similarly for
    reproducible research, it can be time consuming to ensure that you have
    all of the needed packages installed and loaded and that the correct working
    directory is set. 'simpleSetup' provides simple functions for making these
    tasks more straightforward.
	"""
	
	cran = "simpleSetup" 

	version("0.1.0", md5="972c574afd992fbdfb24ea2f11d10193")

