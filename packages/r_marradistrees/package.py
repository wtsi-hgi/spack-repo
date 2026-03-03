# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarradistrees(RPackage):
	"""Plots a Tree-Like Representation of a Numerical Variable
(Marradi's Tree)

	Provides a single function plotting Marradi's trees: a graphical representation
 of a numerical variable for comparing the variable mean and standard deviation across subgroups. See A. Marradi "L'analisi monovariata" (1993, ISBN: 9788820496876).
	"""
	
	cran = "marradistrees" 

	version("1.0", md5="538393db18f1aba299db01f485ce9a18")

