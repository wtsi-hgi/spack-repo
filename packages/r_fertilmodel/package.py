# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFertilmodel(RPackage):
	"""Fertility Models

	Four fertility models are fitted using non-linear least squares. These are the Hadwiger, the Gamma, the Model1 and Model2, following the terminology of the following paper: Peristera P. and Kostaki A. (2007). "Modeling fertility in modern populations". Demographic Research, 16(6): 141--194. <doi:10.4054/DemRes.2007.16.6>. Model based averaging is also supported.
	"""
	
	cran = "fertilmodel" 

	version("1.1", md5="4af6983770956d76a5beb98517a1fec2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
