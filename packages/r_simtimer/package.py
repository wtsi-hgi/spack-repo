# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimtimer(RPackage):
	"""Datetimes as Integers for Discrete-Event Simulations

	Handles datetimes as integers for the usage inside
        Discrete-Event Simulations (DES). The conversion is made using
        the internally generic function as.numeric() of the base
        package. DES is described in Simulation Modeling and Analysis
        by Averill Law and David Kelton (1999) <doi:10.2307/2288169>.
	"""
	
	homepage = "http://github.com/ims-fhs/simtimer"
	cran = "simtimer" 

	version("4.0.0", md5="6927d67f0d34cc00942b1dde833eebc9")

