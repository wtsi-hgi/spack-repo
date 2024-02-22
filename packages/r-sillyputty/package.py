# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSillyputty(RPackage):
	"""Silly Putty Clustering

	Implements a simple, novel clustering algorithm based on
  optimizing the silhouette width. See <doi:10.1101/2023.11.07.566055>
  for details.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "SillyPutty" 

	version("0.4.1", md5="8ea912a949a27bc2524fe9f764170ebd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-thresher", type=("build", "run"))
	depends_on("r-oompabase", type=("build", "run"))
	depends_on("r-polychrome@1.2:", type=("build", "run"))
