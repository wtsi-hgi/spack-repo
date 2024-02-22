# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu19ksubccdf(RPackage):
	"""mu19ksubccdf

	A package containing an environment representing the Mu19KsubC.CDF file.
	"""
	
	bioc = "mu19ksubccdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mu19ksubccdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mu19ksubccdf/mu19ksubccdf_2.18.0.tar.gz"]

	version("2.18.0", md5="e53ef2716f88022e5e41e2cd857fc2a3")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation