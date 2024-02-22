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
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/adductData_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/adductData/adductData_1.18.0.tar.gz"]

	version("1.18.0", md5="bf0e3549ee672a31f32759f0535f360a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-experimenthub@1.9:", type=("build", "run"))
	depends_on("r-annotationhub@2.13.10:", type=("build", "run"))

	# experiment