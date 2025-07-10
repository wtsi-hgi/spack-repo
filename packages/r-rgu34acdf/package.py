# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgu34acdf(RPackage):
	"""rgu34acdf

	A package containing an environment representing the RG_U34A.cdf file.
	"""
	
	bioc = "rgu34acdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rgu34acdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rgu34acdf/rgu34acdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="982f0be8a662d49c8db9dcb8ff18a2de7f42bb73abd29d28afa286db4d70e923")

	depends_on("r-annotationdbi", type=("build", "run"))

