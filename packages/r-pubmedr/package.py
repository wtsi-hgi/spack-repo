# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPubmedr(RPackage):
	"""Gathering Metadata About Publications, Grants, Clinical Trials
from 'PubMed' Database

	A set of tools to extract bibliographic content from 'PubMed' database using 'NCBI' REST API <https://www.ncbi.nlm.nih.gov/home/develop/api/>.
	"""
	
	homepage = "https://github.com/massimoaria/pubmedR"
	cran = "pubmedR" 

	version("0.0.3", md5="e7cdeb02404eb6f0bf1f2173e07d83b1")

	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
