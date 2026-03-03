# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolycrossdesigns(RPackage):
	"""Polycross Designs ("PolycrossDesigns")

	A polycross is the pollination by natural hybridization of a group of genotypes, generally selected, grown in isolation from other compatible genotypes in such a way to promote random open pollination. A particular practical application of the polycross method occurs in the production of a synthetic variety resulting from cross-pollinated plants. Laying out these experiments in appropriate designs, known as polycross designs, would not only save experimental resources but also gather more information from the experiment. Different experimental situations may arise in polycross nurseries which may be requiring different polycross designs (Varghese et. al. (2015) <doi:10.1080/02664763.2015.1043860>. " Experimental designs for open pollination in polycross trials"). This package contains a function named PD() which generates nine types of polycross designs suitable for various experimental situations. 
	"""
	
	cran = "PolycrossDesigns" 

	version("1.1.0", md5="d29072ed4ef30d10dcc2d14546851064")

	depends_on("r@2.10:", type=("build", "run"))
