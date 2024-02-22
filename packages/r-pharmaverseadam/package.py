# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPharmaverseadam(RPackage):
	"""ADaM Test Data for the 'Pharmaverse' Family of Packages

	A set of Analysis Data Model (ADaM) datasets constructed using the 
    Study Data Tabulation Model (SDTM) datasets contained in the 'pharmaversesdtm' package and 
    the template scripts from the 'admiral' family of packages. ADaM dataset specifications are 
    described in: CDISC Analysis Data Model Team
    (2021) <https://www.cdisc.org/system/files/members/standard/foundational/ADaMIG_v1.3.pdf>.
	"""
	
	homepage = "https://pharmaverse.github.io/pharmaverseadam/main/"
	cran = "pharmaverseadam" 

	version("0.2.0", md5="c5bfbce6bc13f645ca195f3c7b5dcc82")

	depends_on("r@3.5:", type=("build", "run"))
