# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsdne(RPackage):
	"""Response Surface Designs with Neighbour Effects (rsdNE)

	Response surface designs with neighbour effects are suitable for experimental situations 
            where it is expected that the treatment combination administered to one experimental unit 
            may affect the response on neighboring units as well as the response on the unit to which it is applied. 
            Integrating these effects in the response surface model improves the experiment's precision 
            (Jaggi, S., Sarika and Sharma, V.K. (2010)<http://krishi.icar.gov.in/jspui/handle/123456789/4364>; 
            Verma A., Jaggi S., Varghese, E.,Varghese, C.,Bhowmik, A., Datta, A. and Hemavathi M. (2021)<DOI: 10.1080/03610918.2021.1890123>). 
            This package includes sym(), asym1(), asym2() functions that generates response surface designs which are rotatable under a 
            polynomial model of a given order without interaction term incorporating neighbour effects. 
	"""
	
	cran = "rsdNE" 

	version("1.1.0", md5="f5be288d184e07713e6fc9ee79237f56")

