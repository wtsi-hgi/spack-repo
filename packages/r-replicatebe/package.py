# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReplicatebe(RPackage):
	"""Average Bioequivalence with Expanding Limits (ABEL)

	Performs comparative bioavailability calculations for Average
    Bioequivalence with Expanding Limits (ABEL). Implemented are 'Method A' /
    'Method B' and the detection of outliers. If the design allows, assessment
    of the empiric Type I Error and iteratively adjusting alpha to control the
    consumer risk. Average Bioequivalence - optionally with a tighter (narrow
    therapeutic index drugs) or wider acceptance range (South Africa: Cmax) -
    is implemented as well.
	"""
	
	homepage = "https://github.com/Helmut01/replicateBE"
	cran = "replicateBE" 

	version("1.1.3", md5="55d2a8e28b82e32a47897aed307c097a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readxl@1:", type=("build", "run"))
	depends_on("r-powertost@1.5.3:", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-pbkrtest", type=("build", "run"))
