# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPov(RPackage):
	"""Partition of Variation Variance Component Analysis Method

	An implementation of the Partition Of variation (POV) method as
    developed by Dr. Thomas A Little <https://thomasalittleconsulting.com> in
    1993 for the analysis of semiconductor data for hard drive manufacturing.
    POV is based on sequential sum of squares and is an exact method that
    explains all observed variation. It quantitates both the between and within
    factor variation effects and can quantitate the influence of both continuous
    and categorical factors.
	"""
	
	homepage = "https://github.com/PaulAntonDeen/POV-R-Package"
	cran = "POV" 

	version("0.1.4", md5="50cc82cbcdad52f2ae71ee6d698a4700")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
