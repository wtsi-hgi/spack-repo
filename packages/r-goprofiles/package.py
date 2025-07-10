# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoprofiles(RPackage):
	"""goProfiles: an R package for the statistical analysis of functional profiles

	The package implements methods to compare lists of genes based on comparing the corresponding 'functional profiles'.
	"""
	
	bioc = "goProfiles" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/goProfiles_1.64.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/goProfiles/goProfiles_1.64.0.tar.gz"]

	version("1.64.0", sha256="7c0a40b2af85298dab153b462266388f6c4e945c2009b7ab8e1d5d5c3abc0892")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
