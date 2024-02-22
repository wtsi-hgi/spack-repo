# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsm(RPackage):
	"""Interpretive Structural Modelling (ISM)

	The development of ISM was made by Warfield in 1974. 
      ISM is the process of collaborating distinct or related essentials into a simplified and an organized format. Hence, ISM is a methodology that seeks the interrelationships among the various elements considered and endows with a hierarchical and multilevel structure.
      To run this package user needs to provide a matrix (VAXO) converted into 0's and 1's.
      Warfield,J.N. (1974) <doi:10.1109/TSMC.1974.5408524>
      Warfield,J.N. (1974, E-ISSN:2168-2909).
	"""
	
	cran = "ISM" 

	version("0.1.0", md5="967ae306c22892f58330fc8d669eb9fc")

	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-xlsxjars", type=("build", "run"))
