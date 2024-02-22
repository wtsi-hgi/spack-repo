# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScsorter(RPackage):
	"""Implementation of 'scSorter' Algorithm

	Implements the algorithm described in
	Guo, H., and Li, J., "scSorter: assigning cells to known cell types according to known marker genes". 
	Cluster cells to known cell types based on marker genes specified for each cell type.
	"""
	
	cran = "scSorter" 

	version("0.0.2", md5="2f53a258af14338a7b2763da28a3e3eb")

	depends_on("r@3.6:", type=("build", "run"))
