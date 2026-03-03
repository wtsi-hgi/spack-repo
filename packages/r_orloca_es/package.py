# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrlocaEs(RPackage):
	"""Spanish version of orloca package. Modelos de localizacion en
investigacion operativa

	Help and demo in Spanish of the orloca package. (Ayuda y demo en espanol del paquete orloca.) Objetos y metodos para manejar y resolver el problema de localizacion de suma minima, tambien conocido como problema de Fermat-Weber. El problema de localizacion de suma minima busca un punto tal que la suma ponderada de las distancias a los puntos de demanda se minimice. Vease "The Fermat-Weber location problem revisited" por Brimberg, Mathematical Programming, 1, pag. 71-76, 1995. <DOI: 10.1007/BF01592245>.
	     Se usan algoritmos generales de optimizacion global para resolver el problema, junto con el metodo adhoc Weiszfeld, vease "Sur le point pour lequel la Somme des distance de n points donnes est minimum", por Weiszfeld, Tohoku Mathematical Journal, First Series, 43, pag. 355-386, 1937 o "On the point for which the sum of the distances to n given points is minimum", por E. Weiszfeld y F. Plastria, Annals of Operations Research, 167, pg. 7-41, 2009. <DOI:10.1007/s10479-008-0352-z>.
	"""
	
	homepage = "http://knuth.uca.es/orloca"
	cran = "orloca.es" 

	version("4.9", md5="998208dc8d48e8e1f1f2f01be918f203")

	depends_on("r-orloca@4.9:", type=("build", "run"))
