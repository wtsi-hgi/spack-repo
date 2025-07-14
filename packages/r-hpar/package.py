# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpar(RPackage):
	"""Human Protein Atlas in R

	The hpar package provides a simple R interface to and data from the Human Protein Atlas project.
	"""
	
	bioc = "hpar" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hpar_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hpar/hpar_1.44.0.tar.gz"]

    version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="087c44020b4f79cd6fea3eb8ed9d29cae784adf796e22f3b2d342b3a30f04da6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
