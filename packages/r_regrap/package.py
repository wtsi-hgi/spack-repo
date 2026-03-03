# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegrap(RPackage):
	"""Reverse Graphical Approaches

	The graphical approach is proposed as a general framework for clinical trial designs involving multiple hypotheses, where decisions are made only based on the observed marginal p-values. A reverse graphical approach starts from a set of singleton graphs, and gradually add vertices into graphs until rejection of a set of hypotheses is made. See Gou, J. (2020). Reverse graphical approaches for multiple test procedures. Technical Report. 
	"""
	
	cran = "regrap" 

	version("1.0.1", md5="58d42f7a53a96a6d4e7a4413bde7483f")

	depends_on("r-mvtnorm", type=("build", "run"))
