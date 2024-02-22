# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoppecosenzar(RPackage):
	"""COPPE-Cosenza Fuzzy Hierarchy Model

	The program implements the COPPE-Cosenza Fuzzy Hierarchy Model. 
    The model was based on the evaluation of local alternatives, representing 
    regional potentialities, so as to fulfill demands of economic projects. 
    After defining demand profiles in terms of their technological coefficients, 
    the degree of importance of factors is defined so as to represent  
    the productive activity. The method can detect a surplus of supply without 
    the restriction of the distance of classical algebra, defining a hierarchy 
    of location alternatives. In COPPE-Cosenza Model, the distance between 
    factors is measured in terms of the difference between grades of memberships
    of the same factors belonging to two or more  sets under comparison. The 
    required factors are classified under the following linguistic variables: 
    Critical (CR); Conditioning (C); Little Conditioning (LC); and Irrelevant 
    (I). And the alternatives can assume the following linguistic variables: 
    Excellent (Ex), Good (G), Regular (R), Weak (W), Empty (Em), Zero (Z) and 
    Inexistent (In). The model also provides flexibility, allowing different 
    aggregation rules to be performed and defined by the Decision Maker. Such 
    feature is considered in this package, allowing the user to define other 
    aggregation matrices, since it considers the same linguistic variables 
    mentioned. 
	"""
	
	homepage = "https://github.com/ptaranti/coppeCosenzaR"
	cran = "coppeCosenzaR" 

	version("0.1.3", md5="cb17131bff17d1698b84c7cea28930b3")

	depends_on("r@3.2.2:", type=("build", "run"))
