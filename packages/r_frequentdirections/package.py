# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrequentdirections(RPackage):
	"""Implementation of Frequent-Directions Algorithm for Efficient
Matrix Sketching

	Implement frequent-directions algorithm for efficient matrix sketching. 
  (Edo Liberty (2013) <doi:10.1145/2487575.2487623>).
	"""
	
	homepage = "https://github.com/shinichi-takayanagi/frequentdirections"
	cran = "frequentdirections" 

	version("0.1.0", md5="e110a6f015478b7ff15f7d660cc7e126")

	depends_on("r-ggplot2", type=("build", "run"))
