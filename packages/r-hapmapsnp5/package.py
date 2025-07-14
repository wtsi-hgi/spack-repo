# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmapsnp5(RPackage):
	"""Sample data - Hapmap SNP 5.0 Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmapsnp5" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hapmapsnp5_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/hapmapsnp5/hapmapsnp5_1.44.0.tar.gz"]

	version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="63c0e6f2940e68c4506c648e0524ea21f18c878af9c38b11ed4d6d4bdb980691", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hapmapsnp5_1.44.0.tar.gz")


