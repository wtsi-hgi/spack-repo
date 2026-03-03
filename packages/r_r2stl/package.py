# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2stl(RPackage):
	"""Visualizing Data using a 3D Printer

	Converts data to STL (stereolithography) files
    that can be used to feed a 3-dimensional printer.  The
    3-dimensional output from a function can be materialized
    into a solid surface in a plastic material, therefore allowing
    more detailed examination. There are many possible uses for
    this new tool, such as to examine mathematical expressions
    with very irregular shapes, to aid teaching people with
    impaired vision, to create raised relief maps from digital
    elevation maps (DEMs), to bridge the gap between mathematical
    tools and rapid prototyping, and many more.  Ian Walker created
    the function r2stl() and Jose' Gama assembled the package.
	"""
	
	homepage = "https://github.com/paulnorthrop/r2stl"
	cran = "r2stl" 

	version("1.0.3", md5="e03d6ef170665e6d12a55cc3c480d266")

	depends_on("r@2.7:", type=("build", "run"))
