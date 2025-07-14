# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFletcher2013b(RPackage):
	"""Master regulators of FGFR2 signalling and breast cancer risk

	This package reproduces the systems biology analysis for the data in package Fletcher2013a using RTN.
	"""
	
	homepage = "http://dx.doi.org/10.1038/ncomms3464"
	bioc = "Fletcher2013b"

	version("1.44.0", commit="6cc90dc662bf1d34e5cbb862fd49dcfddbbebfd2")
	version("1.38.0", commit="40748fbc4bd3a4b6451723544f9658826640c394")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-fletcher2013a", type=("build", "run"))
	depends_on("r-rtn@1.1.2:", type=("build", "run"))
	depends_on("r-reder@1.8.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))

