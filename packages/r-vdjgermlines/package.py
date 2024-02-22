# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdjgermlines(RPackage):
	"""Variable, Diversity and Joining Sequences from Various Species

	Contains variable, diversity, and joining sequences and accompanying functions that enable both the extraction of and comparison between immune V-D-J genomic segments from a variety of species. Sources include IMGT from MP Lefranc (2009) <doi:10.1093/nar/gkn838> and Vgenerepertoire from publication DN Olivieri (2014) <doi:10.1007/s00251-014-0784-3>. 
	"""
	
	cran = "VDJgermlines" 

	version("0.1", md5="2d2d536e5b10355b99166a99d68ff70c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
