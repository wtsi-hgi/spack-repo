# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisposables(RPackage):
	"""Create Disposable R Packages for Testing

	Create disposable R packages for testing.
    You can create, install and load multiple R packages with a single
    function call, and then unload, uninstall and destroy them with another
    function call. This is handy when testing how some R code or an R package
    behaves with respect to other packages.
	"""
	
	homepage = "https://github.com/gaborcsardi/disposables"
	cran = "disposables" 

	version("1.0.3", md5="6ba335441aee883ff2d83435132a1791")

