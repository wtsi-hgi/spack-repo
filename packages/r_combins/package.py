# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombins(RPackage):
	"""Construction Methods of some Series of PBIB Designs

	Series of partially balanced incomplete block designs (PBIB) based on the combinatory method (S) introduced in (Imane Rezgui et al, 2014) <doi:10.3844/jmssp.2014.45.48>; and it gives their associated U-type design.
	"""
	
	homepage = "'www.sites.google.com/site/mohamedlaibwebpage'"
	cran = "CombinS" 

	version("1.1-1", md5="7524991c0354c2ce63d293da4b055cdf")

