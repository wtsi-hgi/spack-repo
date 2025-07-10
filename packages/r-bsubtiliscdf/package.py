# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsubtiliscdf(RPackage):
	"""bsubtiliscdf

	A package containing an environment representing the Bsubtilis.CDF file.
	"""
	
	bioc = "bsubtiliscdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/bsubtiliscdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/bsubtiliscdf/bsubtiliscdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="d4c7c19981cf2e5803090c53dc53ccf898ab917add928c614e649d51a3cc30e6")

	depends_on("r-annotationdbi", type=("build", "run"))

