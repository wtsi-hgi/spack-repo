# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74ccdf(RPackage):
	"""mgu74ccdf

	A package containing an environment representing the MG_U74C.cdf file.
	"""
	
	bioc = "mgu74ccdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74ccdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74ccdf/mgu74ccdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="7275d4aed16350386eb30a023d5cf638b28afbbc8d3d44861539e4b36bd7ab05")

	depends_on("r-annotationdbi", type=("build", "run"))

