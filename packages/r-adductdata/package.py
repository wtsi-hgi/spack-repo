# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdductdata(RPackage):
	"""Data from untargeted MS of modifications to Cys34 of serum albumin

	mzXML files from Grigoryan et al 2016 (Anal Chem).
	"""
	
	bioc = "adductData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/adductData_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/adductData/adductData_1.18.0.tar.gz"]

	version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="a551c63fe130120370b5ce4ce70b43d186ea566c00c1dbe9f399dc523c4f8799")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-experimenthub@1.9:", type=("build", "run"))
	depends_on("r-annotationhub@2.13.10:", type=("build", "run"))

