# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMistat(RPackage):
	"""Data Sets, Functions and Examples from the Book: "Modern
Industrial Statistics" by Kenett, Zacks and Amberti

	Provide all the data sets and statistical analysis applications used in "Modern Industrial Statistics: with applications in R, MINITAB and JMP" by R.S. Kenett and S. Zacks with contributions by D. Amberti, John Wiley and Sons, 2021, which is a third revised and expanded revision of "Modern Industrial Statistics: Design and Control of Quality and Reliability", R. Kenett and S. Zacks, Duxbury/Wadsworth Publishing, 1998.
	"""
	
	cran = "mistat" 

	version("2.0.4", md5="c8077a929a81013e3334891c718ec0d8")

	depends_on("r@3.5:", type=("build", "run"))
