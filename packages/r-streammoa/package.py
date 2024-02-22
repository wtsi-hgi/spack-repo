# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStreammoa(RPackage):
	"""Interface for MOA Stream Clustering Algorithms

	Interface for data stream clustering algorithms implemented in the MOA (Massive Online Analysis) framework (Albert Bifet, Geoff Holmes, Richard Kirkby, Bernhard Pfahringer (2010). MOA: Massive Online Analysis, Journal of Machine Learning Research 11: 1601-1604).
	"""
	
	cran = "streamMOA" 

	version("1.3-0", md5="2d7f235f3a7e1ff444360456d4481880")

	depends_on("r-stream@2.0.0:", type=("build", "run"))
	depends_on("r-rjava@1.0.1:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
