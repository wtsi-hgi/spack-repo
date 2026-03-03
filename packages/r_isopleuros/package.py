# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsopleuros(RPackage):
	"""Ternary Plots

	Ternary plots made simple. This package allows to create
    ternary plots using 'graphics'. It provides functions to display the
    data in the ternary space, to add or tune graphical elements and to
    display statistical summaries. It also includes common ternary
    diagrams which are useful for the archaeologist (e.g. soil texture
    charts, ceramic phase diagram).
	"""
	
	homepage = "https://packages.tesselle.org/isopleuros/"
	cran = "isopleuros" 

	version("1.2.0", md5="c74184bd3369cf0d10704d97440e1bce")

	depends_on("r@3.5:", type=("build", "run"))
