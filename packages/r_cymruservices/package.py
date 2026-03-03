# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCymruservices(RPackage):
	"""Query 'Team Cymru' 'IP' Address, Autonomous System Number
('ASN'), Border Gateway Protocol ('BGP'), Bogon and 'Malware'
Hash Data Services

	A toolkit for querying 'Team Cymru' <http://team-cymru.org> 'IP'
    address, Autonomous System Number ('ASN'), Border Gateway Protocol ('BGP'), Bogon
    and 'Malware' Hash Data Services.
	"""
	
	cran = "cymruservices" 

	version("0.5.0", md5="92bb4435a75b1ed843a8ffb9796c1978")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-pingr", type=("build", "run"))
