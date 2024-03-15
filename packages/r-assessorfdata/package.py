# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssessorfdata(RPackage):
	"""Data and Files for the AssessORF Package

	This package provides access to mapping and results objects generated by the AssessORF package, as well as the genome sequences for the strains corresponding to those objects.
	"""
	
	bioc = "AssessORFData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/AssessORFData_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/AssessORFData/AssessORFData_1.20.0.tar.gz"]

	version("1.20.0", md5="0dd44e672021a9179762efe4959e8608")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-decipher", type=("build", "run"))

	# experiment