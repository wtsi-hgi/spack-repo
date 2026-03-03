# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScifigure(RPackage):
	"""Visualize 'Reproducibility' and 'Replicability' in a Comparison
of Scientific Studies

	Users may specify what fundamental qualities of a new study have 
             or have not changed in an attempt to reproduce or replicate an 
             original study. A comparison of the differences is visualized. 
             Visualization approach follows 'Patil', 'Peng', and 
             'Leek' (2016) <doi:10.1101/066803>.
	"""
	
	cran = "scifigure" 

	version("0.2", md5="bc3a67b5e1cf0d441ea02382be01ce73")

	depends_on("r@3:", type=("build", "run"))
