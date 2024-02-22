# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatisfactory(RPackage):
	"""Statistical and Geometrical Tools

	A collection of statistical and geometrical tools
	including the aligned rank transform (ART; Higgins et al.
	1990 <doi:10.4148/2475-7772.1443>; Peterson 2002
	<doi:10.22237/jmasm/1020255240>; Wobbrock et al. 2011
	<doi:10.1145/1978942.1978963>), 2-D histograms and
	histograms with overlapping bins, a function for making all
	possible formulae within a set of constraints, amongst others.
	"""
	
	homepage = "https://github.com/adamlilith/statisfactory"
	cran = "statisfactory" 

	version("1.0.4", md5="c3ee7256e60eb7f96c80e076ae5e1be0")

	depends_on("r-omnibus", type=("build", "run"))
