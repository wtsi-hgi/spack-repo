# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistory(RPackage):
	"""Distance Between Phylogenetic Histories

	Geodesic distance between phylogenetic trees and
  associated functions. The theoretical background of 'distory'
  is published in Billera et al. (2001) "Geometry of the space of
  phylogenetic trees." <doi:10.1006/aama.2001.0759>.
	"""
	
	cran = "distory" 

	version("1.4.4", md5="2261ea168259e7207bf716180c45605a")

	depends_on("r-ape@5:", type=("build", "run"))
