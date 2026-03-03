# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlantecophys(RPackage):
	"""Modelling and Analysis of Leaf Gas Exchange Data

	Coupled leaf gas exchange model, A-Ci curve simulation and
    fitting, Ball-Berry stomatal conductance models, 
    leaf energy balance using Penman-Monteith, Cowan-Farquhar
    optimization, humidity unit conversions. 
    See Duursma (2015) <doi:10.1371/journal.pone.0143346>.
	"""
	
	homepage = "https://bitbucket.org/remkoduursma/plantecophys"
	cran = "plantecophys" 

	version("1.4-6", md5="a5ca2264dfcb3effc6ae14dc21de5900")

	depends_on("r@3.3:", type=("build", "run"))
