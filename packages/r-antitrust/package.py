# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAntitrust(RPackage):
	"""Tools for Antitrust Practitioners

	A collection of tools for antitrust practitioners, including the ability to calibrate different consumer demand systems and simulate the effects of mergers under different competitive regimes.
	"""
	
	homepage = "https://github.com/luciu5/antitrust"
	cran = "antitrust" 

	version("0.99.26", md5="0dfd1134ae1ef6f752cd46f252367fa5")

	depends_on("r-bb", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
