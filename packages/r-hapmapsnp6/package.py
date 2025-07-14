# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmapsnp6(RPackage):
	"""Sample data - Hapmap SNP 6.0 Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmapsnp6" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hapmapsnp6_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/hapmapsnp6/hapmapsnp6_1.44.0.tar.gz"]

    version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="3604a38b1d9d180051ef874803b9e89f55caca5c4ab0e27a52ac5e52754ba5b7", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hapmapsnp6_1.44.0.tar.gz")

	depends_on("r@2.15:", type=("build", "run"))

