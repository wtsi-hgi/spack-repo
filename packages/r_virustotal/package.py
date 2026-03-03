# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVirustotal(RPackage):
	"""R Client for the VirusTotal API

	Use VirusTotal, a Google service that analyzes files and URLs 
    for viruses, worms, trojans etc., provides category of the content hosted by a 
    domain from a variety of prominent services, provides passive DNS information,
    among other things. See <http://www.virustotal.com> for more information. 
	"""
	
	homepage = "https://github.com/themains/virustotal"
	cran = "virustotal" 

	version("0.2.2", md5="28a20675ebda55e1ca6eb88ebc70ea67")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
