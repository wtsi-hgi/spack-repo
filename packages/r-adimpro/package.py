# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdimpro(RPackage):
	"""Adaptive Smoothing of Digital Images

	Implements tools for manipulation of digital
			 		images and the Propagation Separation approach
			 		by Polzehl and Spokoiny (2006) <DOI:10.1007/s00440-005-0464-1>
						for smoothing digital images, see Polzehl and Tabelow (2007)
						<DOI:10.18637/jss.v019.i01>.
	"""
	
	homepage = "https://www.wias-berlin.de/software/imaging/"
	cran = "adimpro"

	version("0.9.6", md5="afa98eb722e4c9ec50c945b0c459ebcf")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-awsmethods@1.1.1:", type=("build", "run"))
	depends_on("imagemagick", type=("build", "link", "run"))
	depends_on("dcraw", type=("build", "link", "run"))
