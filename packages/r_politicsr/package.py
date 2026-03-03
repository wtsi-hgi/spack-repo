# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoliticsr(RPackage):
	"""Calculating Political System Metrics

	A toolbox to facilitate the calculation of political system indicators for researchers. 
    This package offers a variety of basic indicators related to electoral systems, party systems, elections,
    and parliamentary studies, as well as others. Main references are:
    Loosemore and Hanby (1971) <doi:10.1017/S000712340000925X>;
    Gallagher (1991) <doi:10.1016/0261-3794(91)90004-C>;
    Laakso and Taagepera (1979) <doi:10.1177/001041407901200101>;
    Rae (1968) <doi:10.1177/001041406800100305>;
    Hirschmaņ (1945) <ISBN:0-520-04082-1>;
    Kesselman (1966) <doi:10.2307/1953769>;
    Jones and Mainwaring (2003) <doi:10.1177/13540688030092002>;
    Rice (1925) <doi:10.2307/2142407>;
    Pedersen (1979) <doi:10.1111/j.1475-6765.1979.tb01267.x>;
    SANTOS (2002) <ISBN:85-225-0395-8>.
	"""
	
	cran = "politicsR" 

	version("0.1.0", md5="39f583c6abd5844d591684ab9759706e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
