# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIoanalysis(RPackage):
	"""Input Output Analysis

	Calculates fundamental IO matrices (Leontief, Wassily W. (1951) <doi:10.1038/scientificamerican1051-15>); within period analysis via various rankings and coefficients (Sonis and Hewings (2006) <doi:10.1080/09535319200000013>, Blair and Miller (2009) <ISBN:978-0-521-73902-3>, Antras et al (2012) <doi:10.3386/w17819>, Hummels, Ishii, and Yi (2001) <doi:10.1016/S0022-1996(00)00093-3>); across period analysis with impact analysis (Dietzenbacher, van der Linden, and Steenge (2006) <doi:10.1080/09535319300000017>, Sonis, Hewings, and Guo (2006) <doi:10.1080/09535319600000002>); and a variety of table operators.
	"""
	
	homepage = "http://www.real.illinois.edu"
	cran = "ioanalysis" 

	version("0.3.4", md5="498bc1b9a696b2635c0ed575d513d51b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
