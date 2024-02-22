# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtc(RPackage):
	"""Equivalence to Control

	Treatments of a one-way layout, being equivalent to a control, 
 can be selected with this package. Bonferroni adjusted "two one-sided 
 t-tests" (TOST) and related simultaneous confidence intervals are given for 
 both differences or ratios of means of normally distributed data. For the 
 case of equal variances and balanced sample sizes for the treatment groups, 
 the single-step procedure of Bofinger and Bofinger (1995) 
 <doi:10.1111/j.2517-6161.1995.tb02058.x> can be chosen. For non-normal data, 
 the Wilcoxon test is applied.
	"""
	
	cran = "ETC" 

	version("1.5", md5="fa3a2fdafe8bb8a6051239a067eb88d0")

	depends_on("r-mvtnorm", type=("build", "run"))
