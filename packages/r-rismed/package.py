# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRismed(RPackage):
	"""Download Content from NCBI Databases

	A set of tools to extract bibliographic content from the National
    Center for Biotechnology Information (NCBI) databases, including PubMed. The
    name RISmed is a portmanteau of RIS (for Research Information Systems, a common
    tag format for bibliographic data) and PubMed.
	"""
	
	cran = "RISmed" 

	version("2.3.0", md5="e9f94aa208247c855ff671e343605623")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
