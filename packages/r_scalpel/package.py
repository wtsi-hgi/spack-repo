# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScalpel(RPackage):
	"""Processes Calcium Imaging Data

	Identifies the locations of neurons, and estimates their calcium concentrations over time using the SCALPEL method proposed in Petersen, Ashley; Simon, Noah; Witten, Daniela. SCALPEL: Extracting neurons from calcium imaging data. Ann. Appl. Stat. 12 (2018), no. 4, 2430--2456. <doi:10.1214/18-AOAS1159>. <https://projecteuclid.org/euclid.aoas/1542078051>.
	"""
	
	homepage = "www.ajpete.com/software"
	cran = "scalpel" 

	version("1.0.3", md5="0dad0f61ce31264d7df6f357751986a9")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
	depends_on("r-protoclust", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
