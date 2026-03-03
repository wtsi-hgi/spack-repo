# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKaphom(RPackage):
	"""Test the Homogeneity of Kappa Statistics

	Tests the homogeneity of intraclass kappa statistics obtained from independent studies or a stratified study with binary results. It is desired to compare the kappa statistics obtained in multi-center studies or in a single stratified study to give a common or summary kappa using all available information. If the homogeneity test of these kappa statistics is not rejected, then it is possible to make inferences over a single kappa statistic that summarizes all the studies. Muammer Albayrak, Kemal Turhan, Yasemin Yavuz, Zeliha Aydin Kasap (2019) <doi:10.1080/03610918.2018.1538457> Jun-mo Nam (2003) <doi:10.1111/j.0006-341X.2003.00118.x> Jun-mo Nam (2005) <doi:10.1002/sim.2321>Mousumi Banerjee, Michelle Capozzoli, Laura McSweeney,Debajyoti Sinha (1999) <doi:10.2307/3315487> Allan Donner, Michael Eliasziw, Neil Klar (1996) <doi:10.2307/2533154>.
	"""
	
	cran = "kaphom" 

	version("0.3", md5="0ddfe6dc73bb7819a645483687668a48")

