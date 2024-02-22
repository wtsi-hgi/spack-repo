# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRge(RPackage):
	"""Response from Genotype to Environment

	Compute yield-stability index based on Bayesian methodology, which is useful for analyze multi-environment trials in plant breeding programs. References: Cotes Torres JM, Gonzalez Jaimes EP, and Cotes Torres A (2016) <https://revistas.unimilitar.edu.co/index.php/rfcb/article/view/2037> Seleccion de Genotipos con Alta Respuesta y Estabilidad Fenotipica en Pruebas Regionales: Recuperando el Concepto Biologico. 
	"""
	
	cran = "RGE" 

	version("1.0", md5="8b2412d01471ab277a7f0b5faa08528a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
