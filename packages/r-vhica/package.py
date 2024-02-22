# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVhica(RPackage):
	"""Vertical and Horizontal Inheritance Consistence Analysis

	The "Vertical and Horizontal Inheritance Consistence Analysis" method is described in the following publication: "VHICA: a new method to discriminate between vertical and horizontal transposon transfer: application to the mariner family within Drosophila" by G. Wallau. et al. (2016) <DOI:10.1093/molbev/msv341>. The purpose of the method is to detect horizontal transfers of transposable elements, by contrasting the divergence of transposable element sequences with that of regular genes. 
	"""
	
	cran = "vhica" 

	version("0.2.8", md5="379b6100cbe106e4611ef632c168f6ed")

