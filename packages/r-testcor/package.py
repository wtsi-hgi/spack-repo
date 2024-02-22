# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestcor(RPackage):
	"""FWER and FDR Controlling Procedures for Multiple Correlation
Tests

	
       Different multiple testing procedures for correlation tests are implemented. These procedures were shown to theoretically control asymptotically the Family Wise Error Rate (Roux (2018) <https://tel.archives-ouvertes.fr/tel-01971574v1>) or the False Discovery Rate (Cai & Liu (2016) <doi:10.1080/01621459.2014.999157>). The package gather four test statistics used in correlation testing, four FWER procedures with either single step or stepdown versions, and four FDR procedures.
	"""
	
	cran = "TestCor" 

	version("0.0.2.2", md5="7210184dfd9d3dc097c6fcf694a49dbb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
