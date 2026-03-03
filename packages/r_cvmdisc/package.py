# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvmdisc(RPackage):
	"""Cramer von Mises Tests for Discrete or Grouped Distributions

	Implements Cramer-von Mises Statistics for testing fit to (1) fully specified discrete distributions as described in Choulakian, Lockhart and Stephens (1994) <doi:10.2307/3315828> (2) discrete distributions with unknown parameters that must be estimated from the sample data, see Spinelli & Stephens (1997) <doi:10.2307/3315735> and Lockhart, Spinelli and Stephens (2007) <doi:10.1002/cjs.5550350111> (3) grouped continuous distributions with Unknown Parameters, see Spinelli (2001) <doi:10.2307/3316040>. Maximum likelihood estimation (MLE) is used to estimate the parameters. The package computes the Cramer-von Mises Statistics, Anderson-Darling Statistics and the Watson-Stephens Statistics and their p-values.
	"""
	
	cran = "cvmdisc" 

	version("0.1.0", md5="e228df3568ceb05bb97f8682b22fcf47")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
