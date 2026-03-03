# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgauc(RPackage):
	"""Calculate AUC-type measure when gold standard is continuous and
the corresponding optimal linear combination of variables with
respect to it

	The cgAUC can calculate the AUC-type measure of Obuchowski(2006) when gold standard is continuous, and find the optimal linear combination of variables with respect to this measure.
	"""
	
	cran = "cgAUC" 

	version("1.2.1", md5="dcf7f56b493858135282516605116d1b")

	depends_on("r-rcpp", type=("build", "run"))
