# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfpt(RPackage):
	"""Tools for Modelling of Animal Flight Performance

	Allows estimation and modelling of flight costs in animal (vertebrate) flight,
    implementing the aerodynamic power model described in Klein Heerenbrink et al.
    (2015) <doi:10.1098/rspa.2014.0952>. Taking inspiration from the program
    'Flight', developed by Colin Pennycuick (Pennycuick (2008) "Modelling the flying
    bird". Amsterdam: Elsevier. ISBN 0-19-857721-4), flight performance is estimated
    based on basic morphological measurements such as body mass, wingspan and wing
    area. 'afpt' can be used to make predictions on how animals should adjust their
    flight behaviour and wingbeat kinematics to varying flight conditions.
	"""
	
	homepage = "https://github.com/MarcoKlH/afpt-r/"
	cran = "afpt" 

	version("1.1.0.4", md5="d28f84d9ac8116871ec0aa935e1c1285")

	depends_on("r@4:", type=("build", "run"))
