# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolicdf(RPackage):
	"""ecolicdf

	A package containing an environment representing the Ecoli.CDF file.
	"""
	
	bioc = "ecolicdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ecolicdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ecolicdf/ecolicdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="5663f95ffc0a6c85a95a46742123ac652211ac8b61845ac63465d8e965bee5a1")

	depends_on("r-annotationdbi", type=("build", "run"))

