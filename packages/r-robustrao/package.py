# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustrao(RPackage):
	"""An Extended Rao-Stirling Diversity Index to Handle Missing Data

	A collection of functions to compute the Rao-Stirling diversity index
	(Porter and Rafols, 2009) <DOI:10.1007/s11192-008-2197-2> and its extension to
	acknowledge missing data (i.e.,	uncategorized references) by calculating its
	interval of uncertainty using	mathematical optimization as proposed in Calatrava
	et al. (2016) <DOI:10.1007/s11192-016-1842-4>.
	The Rao-Stirling diversity index is a well-established bibliometric indicator
	to measure the interdisciplinarity of scientific publications. Apart from the
	obligatory dataset of publications with their respective references and	a
	taxonomy of disciplines that categorizes references as well as a measure of
	similarity between the disciplines, the Rao-Stirling diversity index requires
	a complete categorization of all references of a publication into disciplines.
	Thus, it fails for a incomplete categorization; in this case, the robust
	extension has to be used, which encodes the uncertainty caused by missing
	bibliographic data as an uncertainty interval.
	Classification / ACM - 2012: Information systems ~ Similarity measures,
	Theory of computation ~ Quadratic	programming, Applied computing ~ Digital
	libraries and archives.
	"""
	
	homepage = "https://gitlab.com/mc.calatrava.moreno/robustrao.git"
	cran = "robustrao" 

	version("1.0-5", md5="aa1660c274e7830027ab940af1872c65")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-gmp@0.5.12:", type=("build", "run"))
	depends_on("r-iterpc@0.3:", type=("build", "run"))
	depends_on("r-quadprog@1.5.5:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
