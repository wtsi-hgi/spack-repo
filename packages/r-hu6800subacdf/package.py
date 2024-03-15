# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu6800subacdf(RPackage):
	"""hu6800subacdf

	A package containing an environment representing the Hu6800subA.CDF file.
	"""
	
	bioc = "hu6800subacdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu6800subacdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu6800subacdf/hu6800subacdf_2.18.0.tar.gz"]

	version("2.18.0", md5="9e8ec301e066e400564976cd9750297e")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation