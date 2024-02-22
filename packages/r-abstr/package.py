# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbstr(RPackage):
	"""R Interface to the A/B Street Transport System Simulation
Software

	Provides functions to convert origin-destination data,
    represented as straight 'desire lines' in the 'sf' Simple Features
    class system, into JSON files that can be directly imported into
    A/B Street <https://www.abstreet.org>, a free and open source tool
    for simulating urban transport systems and scenarios of change
    <doi:10.1007/s10109-020-00342-2>.
	"""
	
	homepage = "https://github.com/a-b-street/abstr"
	cran = "abstr" 

	version("0.4.1", md5="a5f869dc6e86e7a62266f68fd9c3ec90")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
	depends_on("r-lwgeom@0.2.5:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-od@0.3.1:", type=("build", "run"))
	depends_on("r-sf@1.0.1:", type=("build", "run"))
	depends_on("r-tibble@3.0.6:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
