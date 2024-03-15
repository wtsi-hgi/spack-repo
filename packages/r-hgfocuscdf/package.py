# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgfocuscdf(RPackage):
	"""hgfocuscdf

	A package containing an environment representing the HG-Focus.CDF file.
	"""
	
	bioc = "hgfocuscdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgfocuscdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgfocuscdf/hgfocuscdf_2.18.0.tar.gz"]

	version("2.18.0", md5="9883e53bfd9ddb9ad5f3a9c2e47bbd2c")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation