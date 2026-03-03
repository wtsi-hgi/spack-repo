# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPasadr(RPackage):
	"""An Implementation of Process-Aware Stealthy Attack
Detection(PASAD)

	Anomaly detection method based on the paper "Truth will out: Departure-based process-level detection of stealthy attacks on control systems" from Wissam Aoudi, Mikel Iturbe, and Magnus Almgren (2018) <DOI:10.1145/3243734.3243781>. Also referred to the following implementation: <https://github.com/rahulrajpl/PyPASAD>.
	"""
	
	homepage = "https://github.com/ainsuotain/pasadr"
	cran = "pasadr" 

	version("1.0", md5="f8c7d57d04f7d8dc8dc111307f9536cb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
