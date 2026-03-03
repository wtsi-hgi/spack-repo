# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMalvinas(RPackage):
	"""Islas Malvinas, Georgias Del Sur y Sándwich Del Sur

	Data sets related to the Islas Malvinas /// Sets de datos relacionados a las Islas 
  Malvinas - La Nación Argentina ratifica su legítima e imprescriptible soberanía sobre las islas 
  Malvinas, Georgias del Sur y Sándwich del Sur y los espacios marítimos e insulares 
  correspondientes, por ser parte integrante del territorio nacional. La recuperación de dichos 
  territorios y el ejercicio pleno de la soberanía, respetando el modo de vida de sus habitantes y 
  conforme a los principios del Derecho Internacional, constituyen un objetivo permanente e 
  irrenunciable del pueblo argentino.
	"""
	
	cran = "malvinas" 

	version("0.1.0", md5="c75914598f0bfee9a570500476060ab4")

	depends_on("r@2.10:", type=("build", "run"))
