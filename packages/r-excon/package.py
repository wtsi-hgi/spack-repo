# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcon(RPackage):
	"""Interactive Exploration of Contour Data

	Interactive tools to explore topographic-like data
    sets.  Such data sets take the form of a matrix in which the rows and
    columns provide location/frequency information, and the matrix elements
    contain altitude/response information.  Such data is found in cartography,
    2D spectroscopy and chemometrics.  The functions in this package create
    interactive web pages showing the contoured data, possibly with
    slices from the original matrix parallel to each dimension. The interactive
    behavior is created using the 'D3.js' 'JavaScript' library by Mike Bostock.
	"""
	
	homepage = "https://github.com/bryanhanson/exCon"
	cran = "exCon" 

	version("0.2.5", md5="8668110f4486c322cd295c5cd00406a0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
