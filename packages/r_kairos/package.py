# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKairos(RPackage):
	"""Analysis of Chronological Patterns from Archaeological Count
Data

	A toolkit for absolute and relative dating and analysis of
    chronological patterns. This package includes functions for
    chronological modeling and dating of archaeological assemblages from
    count data. It provides methods for matrix seriation. It also allows
    to compute time point estimates and density estimates of the
    occupation and duration of an archaeological site.
	"""
	
	homepage = "https://packages.tesselle.org/kairos/"
	cran = "kairos" 

	version("2.1.0", md5="3faea02251dd928ef4755dd5b01cd01e")
	version("2.0.2", md5="c93386b7c01b4007f3856a33e8ca8d8f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dimensio@0.6:", type=("build", "run"))
	depends_on("r-aion@1.0.2:", type=("build", "run"))
	depends_on("r-arkhe@1.6:", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
