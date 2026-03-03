# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSettings(RPackage):
	"""Software Option Settings Manager for R

	Provides option settings management that goes
    beyond R's default 'options' function. With this package, users can define
    their own option settings manager holding option names, default values and 
    (if so desired) ranges or sets of allowed option values that will be 
    automatically checked. Settings can then be retrieved, altered and reset 
    to defaults with ease. For R programmers and package developers it offers 
    cloning and merging functionality which allows for conveniently defining 
    global and local options, possibly in a multilevel options hierarchy. See 
    the package vignette for some examples concerning functions, S4 classes, 
    and reference classes. There are convenience functions to reset par() 
    and options() to their 'factory defaults'.
	"""
	
	homepage = "https://github.com/markvanderloo/settings"
	cran = "settings" 

	version("0.2.7", md5="e675298093ab60a9739fa5d99e070dd3")

