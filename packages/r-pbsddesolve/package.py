# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbsddesolve(RPackage):
	"""Solver for Delay Differential Equations

	Functions for solving systems of delay differential equations by
   interfacing with numerical routines written by Simon N. Wood, including
   contributions from Benjamin J. Cairns. These numerical routines first
   appeared in Simon Wood's 'solv95' program. This package includes a vignette
   and a complete user's guide. 'PBSddesolve' originally appeared on CRAN under
   the name 'ddesolve'. That version is no longer supported. The current name
   emphasizes a close association with other 'PBS' packages, particularly
   'PBSmodelling'.
	"""
	
	homepage = "https://github.com/pbs-software/pbs-ddesolve"
	cran = "PBSddesolve" 

	version("1.13.4", md5="42f122577b3189c8eefcde8bd0ac23dd")

	depends_on("r@3.5:", type=("build", "run"))
