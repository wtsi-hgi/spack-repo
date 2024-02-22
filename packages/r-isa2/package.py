# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsa2(RPackage):
	"""The Iterative Signature Algorithm

	The ISA is a biclustering algorithm that finds modules 
  in an input matrix. A module or bicluster is a block of the
  reordered input matrix.
	"""
	
	homepage = "https://github.com/gaborcsardi/ISA"
	cran = "isa2" 

	version("0.3.6", md5="01ce8d5c7bd43fa7fe702cbdaf6863d3", url="https://cran.r-project.org/src/contrib/isa2_0.3.6.tar.gz")

	depends_on("r-lattice", type=("build", "run"))
