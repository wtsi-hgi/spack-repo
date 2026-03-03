# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHadamardr(RPackage):
	"""Hadamard Matrix Generation

	Generates Hadamard matrices using different construction methods. For those who want to generate Hadamard matrix, a generic function, Hadamard_matrix() is provided. For those who want to generate Hadamard matrix using a particular method, separate functions are available. See Horadam (2007, ISBN:9780691119212) Hadamard Matrices and their applications, Princeton University Press for more information on Hadamard Matrices.
	"""
	
	cran = "HadamardR" 

	version("1.0.0", md5="6d35f462de71e416978d5504f03a7782")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
