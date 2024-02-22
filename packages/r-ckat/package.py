# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCkat(RPackage):
	"""Composite Kernel Association Test for Pharmacogenetics Studies

	Composite Kernel Association Test (CKAT) is a flexible and robust kernel machine based approach to jointly test the genetic main effect and gene-treatment interaction effect for a set of single-nucleotide polymorphisms (SNPs) in pharmacogenetics (PGx) assessments embedded within randomized clinical trials.
	"""
	
	cran = "CKAT" 

	version("0.1.0", md5="49e79263606a15f0e5cc102c805a4db6")

	depends_on("r-compquadform", type=("build", "run"))
