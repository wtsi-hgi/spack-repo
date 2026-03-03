# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenoplotr(RPackage):
	"""Plot Publication-Grade Gene and Genome Maps

	Draws gene or genome maps and comparisons between these, in a 
   publication-grade manner. Starting from simple, common files, it will 
   draw postscript or PDF files that can be sent as such to journals.
	"""
	
	homepage = "http://genoplotr.r-forge.r-project.org/"
	cran = "genoPlotR" 

	version("0.8.11", md5="0619865364b4e5fec54a2874ba61236d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
