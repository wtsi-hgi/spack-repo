# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeleganscdf(RPackage):
	"""celeganscdf

	A package containing an environment representing the Celegans.CDF file.
	"""
	
	bioc = "celeganscdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/celeganscdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/celeganscdf/celeganscdf_2.18.0.tar.gz"]

	version("2.18.0", md5="1098cd99bfc5000bf9858e4a3acaf452")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation